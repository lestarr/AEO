"""Gemini agent for AEO assessments using pydantic-ai."""

import os
from pydantic_ai import Agent
from pydantic_ai.models.gemini import GeminiModel
from .base import AssessmentAgent, AssessmentResult


class GeminiAgent(AssessmentAgent):
    """Agent that uses Google's Gemini models via pydantic-ai with built-in search."""

    def __init__(self, api_key: str, model: str = "gemini-2.0-flash-exp"):
        """Initialize Gemini agent.

        Args:
            api_key: Google AI API key
            model: Gemini model to use (2.0+ recommended for search grounding)
        """
        super().__init__(api_key, model)

        # Set API key in environment for pydantic-ai
        os.environ["GEMINI_API_KEY"] = api_key

        # Create pydantic-ai agent with Gemini model
        # Gemini 2.0+ has built-in Google Search grounding
        self.agent = Agent(
            model=GeminiModel(model),
            result_type=AssessmentResult,
            system_prompt=(
                "You are an AEO/GENAI-O strategist who produces evidence-based assessment reports. "
                "Use your built-in web search capabilities to thoroughly research the company. "
                "Search for official websites, marketplaces, analyst coverage, media mentions, and credible sources.\n\n"
                "Provide a comprehensive assessment with inline citations."
            )
        )

    async def assess(self, company_name: str, prompt_template: str) -> AssessmentResult:
        """Perform AEO assessment using Gemini with search grounding.

        Args:
            company_name: Company name to assess
            prompt_template: Assessment prompt template

        Returns:
            Structured assessment result
        """
        # Format prompt with company name
        prompt = self._format_prompt(company_name, prompt_template)

        try:
            # Run agent - Gemini 2.0 automatically uses Google Search when needed
            result = await self.agent.run(prompt)

            return result.data

        except Exception as e:
            raise Exception(f"Gemini assessment failed: {str(e)}") from e
