"""Configuration management for AEO Assessment Tool."""

from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Literal


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

    # Application
    app_name: str = "AEO Assessment Tool"
    debug: bool = False

    # LLM Configuration
    active_llm_provider: Literal["gemini", "openai", "anthropic", "perplexity"] = "gemini"

    # API Keys - all optional, only need the active one
    gemini_api_key: str | None = None
    openai_api_key: str | None = None
    anthropic_api_key: str | None = None
    perplexity_api_key: str | None = None

    # Model names
    gemini_model: str = "gemini-2.0-flash-exp"
    openai_model: str = "gpt-4o"
    anthropic_model: str = "claude-3-7-sonnet-20250219"
    perplexity_model: str = "sonar-pro"

    def get_active_api_key(self) -> str:
        """Get API key for the active provider."""
        key_map = {
            "gemini": self.gemini_api_key,
            "openai": self.openai_api_key,
            "anthropic": self.anthropic_api_key,
            "perplexity": self.perplexity_api_key,
        }

        key = key_map.get(self.active_llm_provider)
        if not key:
            raise ValueError(
                f"API key not configured for provider: {self.active_llm_provider}"
            )
        return key

    def get_active_model(self) -> str:
        """Get model name for the active provider."""
        model_map = {
            "gemini": self.gemini_model,
            "openai": self.openai_model,
            "anthropic": self.anthropic_model,
            "perplexity": self.perplexity_model,
        }
        return model_map[self.active_llm_provider]


# Global settings instance
settings = Settings()
