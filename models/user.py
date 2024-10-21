from models.base import Base, CUDMixin
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import String, BigInteger


class User(CUDMixin):
    __tablename__ = "users"
    username: Mapped[str] = mapped_column(String(255))
    tg_id: Mapped[int] = mapped_column(BigInteger, primary_key=True, unique=True)
