import pathlib

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    telegram_token: str = Field()

    root_path: pathlib.Path = Field(default=pathlib.Path(__file__).parents[1])

    class Config:
        env_file = '.env'
