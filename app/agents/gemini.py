"""Gemini agent for AEO assessments using pydantic-ai."""

import google.generativeai as genai
from .base import AssessmentAgent, AssessmentResult


class GeminiAgent(AssessmentAgent):
    """Agent that uses Google's Gemini models via pydantic-ai."""

    def __init__(self, api_key: str, model: str = "gemini-2.0-flash-exp"):
        """Initialize Gemini agent.

        Args:
            api_key: Google AI API key
            model: Gemini model to use
        """
        super().__init__(api_key, model)
        genai.configure(api_key=api_key)
        self.client = genai.GenerativeModel(
            model_name=model,
            generation_config={
                "temperature": 0.7,
                "top_p": 0.95,
                "max_output_tokens": 8192,
            }
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
            # Note: Gemini's grounding/search is automatic in gemini-2.0-flash-exp
            # Generate response
            response = await self.client.generate_content_async(
                prompt,
                tools=[{"google_search": {}}] if "2.0" in self.model else None
            )

            # Get text response
            response_text = response.text

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
            raise Exception(f"Gemini assessment failed: {str(e)}") from e
