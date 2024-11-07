from datetime import datetime
from schematics.base import BaseSchema
from models.vpn import TypeVPN, StatusVPN, BillingPeriod, Currency


class BaseUserVPNsSchema(BaseSchema):
    vpn_key: str
    status: StatusVPN
    type_VPN: TypeVPN
    expire: datetime
    vpn: str
    tg_user_id: int


class CreateUserVPNsSchema(BaseUserVPNsSchema):
    pass


class ShowUserVPNsSchema(BaseUserVPNsSchema):
    pass


class BaseCountriesSchema(BaseSchema):
    view_country: str
    key_country: str


class ShowCountriesSchema(BaseCountriesSchema):
    pass


class BasePricesSchema(BaseSchema):
    view_price: str
    term: int
    billing_period: BillingPeriod
    price: int
    currency: Currency
    price_key: str
    country_id: int
    is_active: bool


class ShowPricesSchema(BasePricesSchema):
    pass
