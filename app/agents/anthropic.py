"""Anthropic Claude agent for AEO assessments."""

from anthropic import AsyncAnthropic
from .base import AssessmentAgent, AssessmentResult


class AnthropicAgent(AssessmentAgent):
    """Agent that uses Anthropic's Claude models."""

    def __init__(self, api_key: str, model: str = "claude-3-7-sonnet-20250219"):
        """Initialize Anthropic agent.

        Args:
            api_key: Anthropic API key
            model: Claude model to use
        """
        super().__init__(api_key, model)
        self.client = AsyncAnthropic(api_key=api_key)

    async def assess(self, company_name: str, prompt_template: str) -> AssessmentResult:
        """Perform AEO assessment using Claude with extended thinking.

        Args:
            company_name: Company name to assess
            prompt_template: Assessment prompt template

        Returns:
            Structured assessment result
        """
        # Format prompt with company name
        prompt = self._format_prompt(company_name, prompt_template)

        try:
            # Create message with extended thinking if supported
            response = await self.client.messages.create(
                model=self.model,
                max_tokens=8000,
                temperature=0.7,
                system="You are an AEO/GENAI-O strategist who produces evidence-based assessment reports. Research the company thoroughly using available information.",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                # Enable extended thinking for supported models
                thinking={
                    "type": "enabled",
                    "budget_tokens": 10000
                } if "sonnet" in self.model.lower() else None
            )

            # Extract response text from content blocks
            response_text = ""
            for block in response.content:
                if block.type == "text":
                    response_text += block.text

            # Parse into sections
            sections = self._parse_sections(response_text)

            return AssessmentResult(
                snapshot=sections.get("snapshot", "No snapshot available"),
                limitations=sections.get("limitations", "No limitations identified"),
                recommendations=sections.get("recommendations", "No recommendations provided"),
                anti_patterns=sections.get("anti_patterns", "No anti-patterns identified"),
                action_plan=sections.get("action_plan", "No action plan generated"),
                metrics=sections.get("metrics", "No metrics defined"),
                raw_response=response_text
            )

        except Exception as e:
            raise Exception(f"Anthropic assessment failed: {str(e)}") from e
