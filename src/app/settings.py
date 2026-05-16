import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    openai_api_key: str

    class Config:
        env_file = ".env"  # tells Pydantic to read from .env
        env_file_encoding = "utf-8"

    @property
    def cwd(self) -> str:
        """Return the current working directory."""
        return os.getcwd()


# Instantiate settings
settings = Settings()
print(settings.openai_api_key)
print(settings.cwd)
