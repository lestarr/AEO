"""Perplexity agent for AEO assessments using pydantic-ai."""

import os

from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel

from .base import AssessmentAgent, AssessmentResult


class PerplexityAgent(AssessmentAgent):
    """Agent that uses Perplexity's online models via pydantic-ai with built-in search."""

    def __init__(self, api_key: str, model: str = "sonar-pro"):
        """Initialize Perplexity agent.

        Args:
            api_key: Perplexity API key
            model: Perplexity model (sonar, sonar-pro, sonar-reasoning)
        """
        super().__init__(api_key, model)

        # Perplexity uses OpenAI-compatible API with custom base URL
        os.environ["PERPLEXITY_API_KEY"] = api_key

        # Create OpenAI-compatible model pointing to Perplexity
        # Perplexity models have built-in web search - no tools needed
        self.agent = Agent(
            model=OpenAIModel(
                model, base_url="https://api.perplexity.ai", api_key=api_key
            ),
            output_type=AssessmentResult,
            system_prompt=(
                "You are an AEO/GENAI-O strategist who produces evidence-based assessment reports. "
                "Use your built-in web search capabilities to research the company thoroughly. "
                "Search for official websites, marketplaces, analyst coverage, media mentions, and credible sources.\n\n"
                "Provide comprehensive assessment with inline citations from your web searches."
            ),
        )

    async def assess(self, company_name: str, prompt_template: str) -> AssessmentResult:
        """Perform AEO assessment using Perplexity with online search.

        Perplexity automatically searches the web and cites sources.

        Args:
            company_name: Company name to assess
            prompt_template: Assessment prompt template

        Returns:
            Structured assessment result
        """
        # Format prompt with company name
        prompt = self._format_prompt(company_name, prompt_template)

        try:
            # Run agent - Perplexity will automatically use web search
            result = await self.agent.run(prompt)

            return result.data

        except Exception as e:
            raise Exception(f"Perplexity assessment failed: {str(e)}") from e
