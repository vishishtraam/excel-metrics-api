from pydantic_settings import BaseSettings


class AppConfig(BaseSettings):
    DATASET_PATH: str

    class Config:
        env_file = ".env"   # tells Pydantic to load from .env


settings = AppConfig()
