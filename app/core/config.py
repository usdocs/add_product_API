from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'Добавление товара в заказ'
    database_url: str = 'sqlite+aiosqlite:///./fastapi.db'
    secret: str = 'SECRET'


settings = Settings()

# Constants
LIFETIME_SECONDS = 3600
MIN_LEN_PASSWORD = 3
