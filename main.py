import logging
from fastapi import FastAPI
from sqladmin import Admin, ModelView

from core.db_connections import db_helper
from models.user import TgUser
from models.vpn import UserVPNs, Country, Price
import uvicorn

logging.basicConfig(level=logging.INFO)
loger = logging.getLogger()

app = FastAPI(
    docs_url="/api/openapi",
    openapi_url="/api/openapi.json",
)
admin = Admin(app, db_helper.engine)


class UserAdmin(ModelView, model=TgUser):
    name = "User"
    name_plural = "Users"
    column_list = [TgUser.tg_id, TgUser.username]
    column_details_list = [TgUser.tg_id, TgUser.username]


class VPNAdmin(ModelView, model=UserVPNs):
    name = "UserVPN"
    name_plural = "UserVPNs"
    column_list = [UserVPNs.id, UserVPNs.vpn_key, UserVPNs.type_VPN]


class PriceAdmin(ModelView, model=Country):
    name = "Country"
    name_plural = "Countries"
    column_list = [Country.id, Country.key_country, Country.view_country]


class UserVPNAdmin(ModelView, model=Price):
    name = "Price"
    name_plural = "Price"
    column_list = [Price.id, Price.view_price, Price.price, Price.currency]


admin.add_view(UserAdmin)
admin.add_view(VPNAdmin)
admin.add_view(PriceAdmin)
admin.add_view(UserVPNAdmin)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        reload=True,
    )
