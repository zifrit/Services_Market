from models.base import Base
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import String, BigInteger


class User(Base):
    __tablename__ = "users"
    username: Mapped[str] = mapped_column(String(255))
    tg_id: Mapped[int] = mapped_column(BigInteger, primary_key=True, unique=True)
