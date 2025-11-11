"""Base agent interface for AEO assessments using pydantic-ai."""

from abc import ABC, abstractmethod
from pydantic import BaseModel, Field
from typing import Optional


class AssessmentResult(BaseModel):
    """Structured result from an AEO assessment."""

    snapshot: str = Field(
        description="What the engines can already see about the company"
    )
    limitations: str = Field(
        description="What limits inclusion inside AI answers"
    )
    recommendations: str = Field(
        description="What 'good' looks like and how to get there"
    )
    anti_patterns: str = Field(
        description="Anti-patterns to stop or fix"
    )
    action_plan: str = Field(
        description="30-45 day plan with specific actions"
    )
    metrics: str = Field(
        description="How we'll measure whether this worked"
    )


class AssessmentAgent(ABC):
    """Base class for LLM agents that perform AEO assessments using pydantic-ai."""

    def __init__(self, api_key: str, model: str):
        """Initialize the agent with API credentials.

        Args:
            api_key: API key for the LLM provider
            model: Model identifier to use
        """
        self.api_key = api_key
        self.model = model

    @abstractmethod
    async def assess(self, company_name: str, prompt_template: str) -> AssessmentResult:
        """Perform an AEO assessment for a company.

        Args:
            company_name: Name of the company to assess
            prompt_template: System prompt template with {company_name} placeholder

        Returns:
            AssessmentResult with structured findings

        Raises:
            Exception: If the assessment fails
        """
        pass

    def _format_prompt(self, company_name: str, prompt_template: str) -> str:
        """Format the prompt template with the company name.

        Args:
            company_name: Company name to inject
            prompt_template: Template with {company_name} placeholder

        Returns:
            Formatted prompt string
        """
        return prompt_template.replace("{company_name}", company_name)
