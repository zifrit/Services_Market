import typing
from models.base import IdCUDMixin
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String, BigInteger

if typing.TYPE_CHECKING:
    from models.vpn import UserVPNs
    from models.referral import Referral
    from models.order import Order


class TgUser(IdCUDMixin):
    __tablename__ = "tg_users"
    username: Mapped[str] = mapped_column(String(255))
    tg_id: Mapped[int] = mapped_column(BigInteger, unique=True)
    user_vpn_s: Mapped[list["UserVPNs"]] = relationship(back_populates="tg_user")
    # Рефералы, которых пригласил данный пользователь
    referred_users: Mapped[list["Referral"]] = relationship(
        "Referral",
        back_populates="referrer",
        foreign_keys="[Referral.referrer_id]",
    )
    # Пользователь, который пригласил текущего пользователя
    invited_by: Mapped[list["Referral"]] = relationship(
        "Referral",
        back_populates="referred_user",
        foreign_keys="[Referral.referred_user_id]",
    )
    orders: Mapped[list["Order"]] = relationship(back_populates="tg_user")

    repr_columns = ["tg_id", "username"]
