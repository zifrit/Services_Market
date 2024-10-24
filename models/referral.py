import typing
from models.base import IdCUDMixin
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String, BigInteger, ForeignKey

if typing.TYPE_CHECKING:
    from models.user import User


class Referral(IdCUDMixin):
    __tablename__ = "referral"
    # Реферал, который пригласил данный пользователь
    # Тот кого пригласили
    referrer_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    # Пользователь, который пригласил текущего пользователя
    # Тот кто пригласил
    referred_user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    referrer: Mapped["User"] = relationship(
        back_populates="referred_users",
        foreign_keys=[referrer_id],
    )

    referred_user: Mapped["User"] = relationship(
        back_populates="invited_by",
        foreign_keys=[referred_user_id],
    )
