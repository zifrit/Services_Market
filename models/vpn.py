import typing
import enum
from models.base import IdCUDMixin
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String, ForeignKey, UniqueConstraint, Integer
from sqlalchemy.dialects.postgresql import ENUM as PGEnum

if typing.TYPE_CHECKING:
    from models.user import User


class StatusUserVPN(enum.Enum):
    active = "active"
    inactive = "inactive"
    pause = "pause"


class UserVPN(IdCUDMixin):
    __tablename__ = "user_vpn"
    view: Mapped[str] = mapped_column(String(255))
    status: Mapped[StatusUserVPN] = mapped_column(
        PGEnum(StatusUserVPN, name="status_user_vpn"),
        comment="Состояние купленного впн",
        default=StatusUserVPN.inactive,
    )
    price_id: Mapped[int] = mapped_column(ForeignKey("price.id"))
    price: Mapped["Price"] = relationship(back_populates="user_vpn_s")
    tg_user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    tg_user: Mapped["User"] = relationship(back_populates="user_vpn")

    repr_columns = ["id", "view"]


class VPN(IdCUDMixin):
    __tablename__ = "vpn"
    country_view_text: Mapped[str] = mapped_column(String(255))
    key_country: Mapped[str] = mapped_column(String(255), unique=True)
    prices: Mapped[list["Price"]] = relationship(
        back_populates="vpn",
    )

    repr_columns = ["id", "country_view_text"]


class Term(enum.Enum):
    day = "day"
    month = "month"
    year = "year"


class Price(IdCUDMixin):
    __tablename__ = "price"
    price_view_text: Mapped[str] = mapped_column(String(255))
    price: Mapped[int]
    quantity: Mapped[int]
    term: Mapped[Term] = mapped_column(
        PGEnum(Term, name="price_term"),
        comment="Вид времени",
    )
    key_price: Mapped[str | None] = mapped_column(
        String(255), comment="Ключ для цены", unique=True
    )
    vpn_id: Mapped[int] = mapped_column(ForeignKey("vpn.id"))
    vpn: Mapped["VPN"] = relationship(back_populates="prices")
    user_vpn_s: Mapped["UserVPN"] = relationship(back_populates="price")

    repr_columns = ["id", "price_view_text", "quantity", "term"]


# class AssociationVPNPrice(IdCUDMixin):
#     __tablename__ = "association_vpn_price"
#     __table_args__ = (
#         UniqueConstraint("vpn_id", "price_id", name="idx_unique_order_product"),
#     )
#     vpn_id: Mapped[int] = mapped_column(ForeignKey("vpn.id"))
#     price_id: Mapped[int] = mapped_column(ForeignKey("price.id"))

# vpn: Mapped["VPN"] = relationship(back_populates="price")
# price: Mapped["Price"] = relationship(back_populates="vpn")
