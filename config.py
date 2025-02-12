from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    auth0_domain: str = "test.auth0.com"
    auth0_api_audience: str = "https://test.auth0.com/api/v2/"
    auth0_issuer: str = "https://test.auth0.com/"
    auth0_algorithms: str = "RS256"


settings = Settings()
