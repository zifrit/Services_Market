import typing

from models.base import IdCUDMixin
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String, BigInteger, ForeignKey

if typing.TYPE_CHECKING:
    from models.user import User


class VPN(IdCUDMixin):
    __tablename__ = "vpn"
    price: Mapped[str] = mapped_column(String(255))
    country: Mapped[str] = mapped_column(String(255))
    tg_user_id: Mapped[int] = mapped_column(ForeignKey("users.tg_id"))
    tg_user: Mapped["User"] = relationship(back_populates="vpn")
