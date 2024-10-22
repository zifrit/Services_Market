import typing
from models.base import Base, CUDMixin
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String, BigInteger

if typing.TYPE_CHECKING:
    from models.vpn import VPN


class User(CUDMixin):
    __tablename__ = "users"
    username: Mapped[str] = mapped_column(String(255))
    tg_id: Mapped[int] = mapped_column(BigInteger, primary_key=True, unique=True)
    vpn: Mapped[list["VPN"]] = relationship(back_populates="tg_user")
