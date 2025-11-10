"""Base agent interface for AEO assessments."""

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
    raw_response: Optional[str] = Field(
        default=None,
        description="Full raw response from the LLM"
    )


class AssessmentAgent(ABC):
    """Base class for LLM agents that perform AEO assessments."""

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

    def _parse_sections(self, response_text: str) -> dict[str, str]:
        """Parse response text into structured sections.

        This is a fallback parser if structured output fails.

        Args:
            response_text: Raw LLM response

        Returns:
            Dictionary with section keys and content
        """
        sections = {
            "snapshot": "",
            "limitations": "",
            "recommendations": "",
            "anti_patterns": "",
            "action_plan": "",
            "metrics": ""
        }

        # Define section headers to look for
        section_markers = {
            "snapshot": ["### Snapshot:", "## Snapshot:", "Snapshot:"],
            "limitations": ["### The catch:", "## The catch:", "The catch:"],
            "recommendations": ["### What \"good\" looks like", "## What \"good\" looks like", "What \"good\" looks like"],
            "anti_patterns": ["### Anti-patterns", "## Anti-patterns", "Anti-patterns"],
            "action_plan": ["### 30–45 day plan", "### 30-45 day plan", "## 30–45 day plan", "30–45 day plan"],
            "metrics": ["### How we'll measure", "## How we'll measure", "How we'll measure"]
        }

        lines = response_text.split("\n")
        current_section = None
        current_content = []

        for line in lines:
            # Check if this line is a section header
            matched_section = None
            for section_key, markers in section_markers.items():
                if any(marker in line for marker in markers):
                    matched_section = section_key
                    break

            if matched_section:
                # Save previous section
                if current_section and current_content:
                    sections[current_section] = "\n".join(current_content).strip()

                # Start new section
                current_section = matched_section
                current_content = []
            elif current_section:
                # Accumulate content for current section
                current_content.append(line)

        # Save last section
        if current_section and current_content:
            sections[current_section] = "\n".join(current_content).strip()

        return sections
