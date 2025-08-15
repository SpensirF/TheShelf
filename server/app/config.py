from pydantic_settings import BaseSettings, SettingsConfigDict

# define a settings container
class Settings(BaseSettings):
    # tell Pydantic where to read env values from
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    DATABASE_URL: str
    JWT_SECRET: str
    JWT_ALG: str = "HS256"

    # Optional now; used later
    S3_BUCKET: str = ""
    AWS_ACCESS_KEY_ID: str = ""
    AWS_SECRET_ACCESS_KEY: str = ""

settings = Settings()