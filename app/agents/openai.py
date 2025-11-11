"""OpenAI agent for AEO assessments using pydantic-ai."""

import os
from pydantic_ai import Agent, WebSearchTool
from pydantic_ai.models.openai import OpenAIModel
from .base import AssessmentAgent, AssessmentResult


class OpenAIAgent(AssessmentAgent):
    """Agent that uses OpenAI models via pydantic-ai with built-in web search."""

    def __init__(self, api_key: str, model: str = "gpt-4o"):
        """Initialize OpenAI agent.

        Args:
            api_key: OpenAI API key
            model: Model to use (gpt-4o, o1-preview, etc.)
        """
        super().__init__(api_key, model)

        # Set API key in environment for pydantic-ai
        os.environ["OPENAI_API_KEY"] = api_key

        # Create pydantic-ai agent with OpenAI model and web search tool
        # Note: OpenAI requires Responses API for web search
        self.agent = Agent(
            model=OpenAIModel(model),
            result_type=AssessmentResult,
            system_prompt=(
                "You are an AEO/GENAI-O strategist who produces evidence-based assessment reports. "
                "Use the web search tool to thoroughly research the company. "
                "Search for official websites, marketplaces, analyst coverage, media mentions, and credible sources.\n\n"
                "Provide comprehensive assessment with inline citations from your searches."
            ),
            builtin_tools=[
                WebSearchTool(
                    search_context_size='high',
                    max_uses=10
                )
            ]
        )

    async def assess(self, company_name: str, prompt_template: str) -> AssessmentResult:
        """Perform AEO assessment using OpenAI with web search.

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
            result = await self.agent.run(prompt)

            return result.data

        except Exception as e:
            raise Exception(f"OpenAI assessment failed: {str(e)}") from e
