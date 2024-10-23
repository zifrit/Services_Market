import typing
from models.base import IdCUDMixin
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String, BigInteger

if typing.TYPE_CHECKING:
    from models.vpn import UserVPN
    from models.referral import Referral


class User(IdCUDMixin):
    __tablename__ = "users"
    username: Mapped[str] = mapped_column(String(255))
    tg_id: Mapped[int] = mapped_column(BigInteger, unique=True)
    user_vpn: Mapped[list["UserVPN"]] = relationship(back_populates="tg_user")
    referred_users: Mapped[list["Referral"]] = relationship(
        "Referral",
        back_populates="referrer",
        foreign_keys="[Referral.referrer_id]",
    )
    invited_by: Mapped[list["Referral"]] = relationship(
        "Referral",
        back_populates="referred_user",
        foreign_keys="[Referral.referred_user_id]",
    )
