import typing

from models.base import IdCUDMixin
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String, BigInteger, ForeignKey, UniqueConstraint

if typing.TYPE_CHECKING:
    from models.user import User


class UserVPN(IdCUDMixin):
    __tablename__ = "user_vpn"
    price: Mapped[str] = mapped_column(String(255))
    country: Mapped[str] = mapped_column(String(255))
    tg_user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    tg_user: Mapped["User"] = relationship(back_populates="user_vpn")

    def __str__(self) -> str:
        return f"{self.price} {self.country}"

    def __repr__(self) -> str:
        return str(self)


class VPN(IdCUDMixin):
    __tablename__ = "vpn"
    country_view_text: Mapped[str] = mapped_column(String(255))
    country: Mapped[str] = mapped_column(String(255))
    price: Mapped[list["Price"]] = relationship(
        secondary="association_vpn_price",
        back_populates="vpn",
    )


class Price(IdCUDMixin):
    __tablename__ = "price"
    price_view_text: Mapped[str] = mapped_column(String(255))
    price: Mapped[str] = mapped_column(String(255))
    vpn: Mapped[list["VPN"]] = relationship(
        secondary="association_vpn_price",
        back_populates="price",
    )


class AssociationVPNPrice(IdCUDMixin):
    __tablename__ = "association_vpn_price"
    __table_args__ = (
        UniqueConstraint("vpn_id", "price_id", name="idx_unique_order_product"),
    )
    vpn_id: Mapped[int] = mapped_column(ForeignKey("vpn.id"))
    price_id: Mapped[int] = mapped_column(ForeignKey("price.id"))

    # vpn: Mapped["VPN"] = relationship(back_populates="price")
    # price: Mapped["Price"] = relationship(back_populates="vpn")
