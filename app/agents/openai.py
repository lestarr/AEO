"""OpenAI agent for AEO assessments."""

from openai import AsyncOpenAI
from .base import AssessmentAgent, AssessmentResult


class OpenAIAgent(AssessmentAgent):
    """Agent that uses OpenAI models (GPT-4, o1, etc.)."""

    def __init__(self, api_key: str, model: str = "gpt-4o"):
        """Initialize OpenAI agent.

        Args:
            api_key: OpenAI API key
            model: Model to use (gpt-4o, gpt-4-turbo, o1-preview, etc.)
        """
        super().__init__(api_key, model)
        self.client = AsyncOpenAI(api_key=api_key)

        # o1 models have different parameters
        self.is_o1 = "o1" in model

    async def assess(self, company_name: str, prompt_template: str) -> AssessmentResult:
        """Perform AEO assessment using OpenAI.

        Args:
            company_name: Company name to assess
            prompt_template: Assessment prompt template

        Returns:
            Structured assessment result
        """
        # Format prompt with company name
        prompt = self._format_prompt(company_name, prompt_template)

        try:
            # Prepare messages
            if self.is_o1:
                # o1 models don't support system messages
                messages = [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
                # o1 models have different parameters
                response = await self.client.chat.completions.create(
                    model=self.model,
                    messages=messages,
                    max_completion_tokens=16000,
                )
            else:
                # Standard models with system prompt
                messages = [
                    {
                        "role": "system",
                        "content": "You are an AEO/GENAI-O strategist who produces evidence-based assessment reports. You have access to web search to research companies."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
                response = await self.client.chat.completions.create(
                    model=self.model,
                    messages=messages,
                    temperature=0.7,
                    max_tokens=8000,
                )

            # Extract response text
            response_text = response.choices[0].message.content

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
            raise Exception(f"OpenAI assessment failed: {str(e)}") from e
