import os
from pydantic_settings import BaseSettings, SettingsConfigDict

env_file_path = os.path.join(os.path.dirname(__file__), '..', '.env')

if not os.path.exists(env_file_path):
    raise FileNotFoundError(f"Error: The environment file '{env_file_path}' was not found. "
                            "Please ensure the .env file is provided at runtime.")


class Settings(BaseSettings):
    app_name: str
    api_domain: str
    website_domain: str
    api_base_path: str
    website_base_path: str
    supertokens_connection_uri: str

    model_config = SettingsConfigDict(
        env_file=env_file_path,
        env_file_encoding='utf-8'
    )
