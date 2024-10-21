from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Postgres(BaseSettings):
    DB_HOST: str = "localhost"
    DB_PORT: int = "5432"
    DB_USER: str = "postgres"
    DB_PASS: str = "postgres"
    DB_NAME: str = "vpn_market"

    @property
    def database_url_asyncpg(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

db_settings = Postgres()