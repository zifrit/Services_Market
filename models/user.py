import typing
from models.base import IdCUDMixin
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String, BigInteger

if typing.TYPE_CHECKING:
    from models.vpn import UserVPN


class User(IdCUDMixin):
    __tablename__ = "users"
    username: Mapped[str] = mapped_column(String(255))
    tg_id: Mapped[int] = mapped_column(BigInteger, unique=True)
    user_vpn: Mapped[list["UserVPN"]] = relationship(back_populates="tg_user")
