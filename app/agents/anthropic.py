"""Anthropic Claude agent for AEO assessments using pydantic-ai."""

import os
import httpx
from pydantic_ai import Agent, RunContext
from pydantic_ai.models.anthropic import AnthropicModel
from .base import AssessmentAgent, AssessmentResult


async def web_search(ctx: RunContext[None], query: str) -> str:
    """Simple web search tool using DuckDuckGo HTML.

    Args:
        ctx: Run context
        query: Search query

    Returns:
        Search results as text
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                "https://html.duckduckgo.com/html/",
                params={"q": query},
                headers={"User-Agent": "Mozilla/5.0"},
                timeout=10.0
            )
            # Return snippet of results (simplified)
            text = response.text[:3000]  # Limit size
            return f"Search results for '{query}':\n{text}"
    except Exception as e:
        return f"Search failed: {str(e)}"


class AnthropicAgent(AssessmentAgent):
    """Agent that uses Anthropic's Claude models via pydantic-ai with web search."""

    def __init__(self, api_key: str, model: str = "claude-3-7-sonnet-20250219"):
        """Initialize Anthropic agent.

        Args:
            api_key: Anthropic API key
            model: Claude model to use
        """
        super().__init__(api_key, model)

        # Set API key in environment for pydantic-ai
        os.environ["ANTHROPIC_API_KEY"] = api_key

        # Create pydantic-ai agent with Anthropic model
        self.agent = Agent(
            model=AnthropicModel(model),
            result_type=AssessmentResult,
            system_prompt=(
                "You are an AEO/GENAI-O strategist who produces evidence-based assessment reports. "
                "Use the web_search tool to research the company thoroughly. "
                "Search for the company's official website, presence on marketplaces, "
                "analyst coverage, media mentions, and other credible sources.\n\n"
                "Structure your response with these exact sections:\n"
                "1. snapshot: what the engines can already see\n"
                "2. limitations: what limits inclusion inside AI answers\n"
                "3. recommendations: what 'good' looks like (and how to get there)\n"
                "4. anti_patterns: anti-patterns to stop or fix\n"
                "5. action_plan: 30-45 day plan (high-impact, doable)\n"
                "6. metrics: how we'll measure whether this worked\n\n"
                "Each section should be comprehensive with inline citations."
            ),
            tools=[web_search]
        )

    async def assess(self, company_name: str, prompt_template: str) -> AssessmentResult:
        """Perform AEO assessment using Claude with web search.

        Args:
            company_name: Company name to assess
            prompt_template: Assessment prompt template

        Returns:
            Structured assessment result
        """
        # Format prompt with company name
        prompt = self._format_prompt(company_name, prompt_template)

        try:
            # Run agent with pydantic-ai
            # Claude 3.7 Sonnet supports extended thinking automatically
            result = await self.agent.run(prompt)

            return result.data

        except Exception as e:
            raise Exception(f"Anthropic assessment failed: {str(e)}") from e
