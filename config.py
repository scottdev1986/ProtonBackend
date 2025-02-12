from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

    auth0_domain: str = None
    auth0_api_audience: str = None
    auth0_issuer: str = None
    auth0_algorithms: str = None

settings = Settings()
