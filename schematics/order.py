from schematics.base import BaseSchema
from models.order import PaymentsStatus
from models.vpn import Currency
from schematics.vpn import ShortShowPriceSchema


class BaseOrderSchema(BaseSchema):
    price_id: int
    tg_user_id: int
    status: bool


class CreateOrderSchema(BaseOrderSchema):
    pass


class ShowOrderSchema(BaseOrderSchema):
    price: ShortShowPriceSchema


class BasePaymentSchema(BaseSchema):
    currency: Currency
    status: PaymentsStatus
    amount: int
    order_id: int


class CreatePaymentSchema(BasePaymentSchema):
    pass


class ShowPaymentSchema(BasePaymentSchema):
    pass
