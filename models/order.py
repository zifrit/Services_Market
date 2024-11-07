import typing
import enum
from datetime import datetime
from models.base import IdCUDMixin
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import ENUM as PGEnum
from models.vpn import Currency

if typing.TYPE_CHECKING:
    from models.user import TgUser
    from models.vpn import Price


class Order(IdCUDMixin):
    __tablename__ = "orders"

    price_id: Mapped[int] = mapped_column(ForeignKey("prices.id"))
    price: Mapped["Price"] = relationship(back_populates="orders")
    tg_user_id: Mapped[int] = mapped_column(ForeignKey("tg_users.id"))
    tg_user: Mapped["TgUser"] = relationship(back_populates="orders")
    status: Mapped[bool] = mapped_column(comment="Статус заказа")
    payments: Mapped["Payment"] = relationship(back_populates="order")

    repr_columns = ["id", "status"]


class PaymentsStatus(enum.Enum):
    completed = "completed"
    failed = "failed"
    in_progress = "in_progress"


class Payment(IdCUDMixin):
    __tablename__ = "payments"

    currency: Mapped[Currency] = mapped_column(
        PGEnum(Currency, name="payment_currency"),
        comment="Валюта",
    )
    status: Mapped[PaymentsStatus] = mapped_column(
        PGEnum(Currency, name="payment_status"),
        comment="Статус платежа",
    )
    amount: Mapped[int] = mapped_column(comment="Сумма")
    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id"))
    order: Mapped["Order"] = relationship(back_populates="payments")
