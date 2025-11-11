"""Anthropic Claude agent for AEO assessments using pydantic-ai."""

import os
from pydantic_ai import Agent, WebSearchTool
from pydantic_ai.models.anthropic import AnthropicModel
from .base import AssessmentAgent, AssessmentResult


class AnthropicAgent(AssessmentAgent):
    """Agent that uses Anthropic's Claude models via pydantic-ai with built-in web search."""

    def __init__(self, api_key: str, model: str = "claude-3-7-sonnet-20250219"):
        """Initialize Anthropic agent.

        Args:
            api_key: Anthropic API key
            model: Claude model to use
        """
        super().__init__(api_key, model)

        # Set API key in environment for pydantic-ai
        os.environ["ANTHROPIC_API_KEY"] = api_key

        # Create pydantic-ai agent with Anthropic model and web search tool
        self.agent = Agent(
            model=AnthropicModel(model),
            result_type=AssessmentResult,
            system_prompt=(
                "You are an AEO/GENAI-O strategist who produces evidence-based assessment reports. "
                "Use the web search tool to thoroughly research the company. "
                "Search for official websites, marketplaces, analyst coverage, media mentions, and credible sources.\n\n"
                "Use your extended thinking capabilities combined with web research to provide "
                "comprehensive assessment with inline citations."
            ),
            builtin_tools=[
                WebSearchTool(
                    search_context_size='high',
                    max_uses=10
                )
            ]
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
