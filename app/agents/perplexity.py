"""Perplexity agent for AEO assessments with online search."""

from openai import AsyncOpenAI
from .base import AssessmentAgent, AssessmentResult


class PerplexityAgent(AssessmentAgent):
    """Agent that uses Perplexity's online models with built-in search."""

    def __init__(self, api_key: str, model: str = "sonar-pro"):
        """Initialize Perplexity agent.

        Args:
            api_key: Perplexity API key
            model: Perplexity model (sonar, sonar-pro, sonar-reasoning)
        """
        super().__init__(api_key, model)
        # Perplexity uses OpenAI-compatible API
        self.client = AsyncOpenAI(
            api_key=api_key,
            base_url="https://api.perplexity.ai"
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
            # Perplexity models have built-in web search
            response = await self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": "You are an AEO/GENAI-O strategist who produces evidence-based assessment reports. Use your web search capabilities to research the company thoroughly."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
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
            raise Exception(f"Perplexity assessment failed: {str(e)}") from e
