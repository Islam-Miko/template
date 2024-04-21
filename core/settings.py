from functools import cache

from pydantic_settings import BaseSettings, SettingsConfigDict

from enum import Enum


class Environment(str, Enum):
    LOCAL = "LOCAL"
    TESTING = "TESTING"
    STAGING = "STAGING"
    PRODUCTION = "PRODUCTION"

    @property
    def is_debug(self):
        return self in (self.LOCAL, self.STAGING, self.TESTING)

    @property
    def is_testing(self):
        return self == self.TESTING

    @property
    def is_deployed(self) -> bool:
        return self in (self.STAGING, self.PRODUCTION)


class Settings(BaseSettings):
    REDIS_URL: str
    POSTGRES_URL: str
    ENVIRONMENT: Environment = Environment.PRODUCTION

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
    
@cache
def get_settings() -> Settings:
    return Settings()