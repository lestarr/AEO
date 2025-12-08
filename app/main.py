"""Main FastAPI application for AEO Assessment Tool."""

import os
from datetime import datetime
from pathlib import Path

from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .agents import AnthropicAgent, GeminiAgent, OpenAIAgent, PerplexityAgent
from .config import settings

# Initialize FastAPI app
app = FastAPI(
    title="AEO Assessment Tool",
    description="Free AI Engine Optimization assessments for companies",
    version="1.0.0",
)

# Setup templates
templates = Jinja2Templates(directory="app/templates")

# Load prompt template
PROMPT_PATH = Path("prompts/aeo_narrative.txt")
with open(PROMPT_PATH, "r", encoding="utf-8") as f:
    PROMPT_TEMPLATE = f.read()


def get_agent():
    """Get the configured LLM agent based on settings.

    Returns:
        Initialized agent instance

    Raises:
        ValueError: If provider is not configured or unsupported
    """
    provider = settings.active_llm_provider
    api_key = settings.get_active_api_key()
    model = settings.get_active_model()

    agent_map = {
        "gemini": GeminiAgent,
        "openai": OpenAIAgent,
        "anthropic": AnthropicAgent,
        "perplexity": PerplexityAgent,
    }

    if provider not in agent_map:
        raise ValueError(f"Unsupported LLM provider: {provider}")

    return agent_map[provider](api_key=api_key, model=model)


# Store the last assessment in memory (MVP - no database)
last_assessment = {
    "company_name": None,
    "result": None,
    "timestamp": None,
    "provider": None,
}


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """Landing page with assessment form or results.

    If an assessment was just completed, show results.
    Otherwise, show the form.
    """
    if last_assessment["result"] is not None:
        # Show report
        return templates.TemplateResponse(
            "report.html",
            {
                "request": request,
                "company_name": last_assessment["company_name"],
                "result": last_assessment["result"],
                "timestamp": last_assessment["timestamp"],
                "provider": last_assessment["provider"],
            },
        )
    else:
        # Show form
        return templates.TemplateResponse("index.html", {"request": request})


@app.post("/assess")
async def assess(company_name: str = Form(...)):
    """Generate AEO assessment for a company.

    Args:
        company_name: Company name from form

    Returns:
        Redirects to index with results

    Raises:
        HTTPException: If assessment fails
    """
    try:
        # Get configured agent
        agent = get_agent()

        # Run assessment
        result = await agent.assess(
            company_name=company_name, prompt_template=PROMPT_TEMPLATE
        )

        # Store in memory
        last_assessment["company_name"] = company_name
        last_assessment["result"] = result
        last_assessment["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        last_assessment["provider"] = settings.active_llm_provider

        # Return success (frontend will reload page)
        return {"status": "success"}

    except Exception as e:
        # Clear any partial results
        last_assessment["result"] = None
        raise Exception(f"Assessment failed: {str(e)}")


@app.get("/health")
async def health():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "provider": settings.active_llm_provider,
        "model": settings.get_active_model(),
    }


@app.get("/reset")
async def reset():
    """Reset the last assessment (for testing)."""
    last_assessment["company_name"] = None
    last_assessment["result"] = None
    last_assessment["timestamp"] = None
    last_assessment["provider"] = None
    return {"status": "reset"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
