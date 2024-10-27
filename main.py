import logging
from fastapi import FastAPI
from sqladmin import Admin, ModelView

from core.db_connections import db_helper
from models.user import User
from models.vpn import UserVPN, VPN, Price
import uvicorn

logging.basicConfig(level=logging.INFO)
loger = logging.getLogger()

app = FastAPI(
    docs_url="/api/openapi",
    openapi_url="/api/openapi.json",
)
admin = Admin(app, db_helper.engine)


class UserAdmin(ModelView, model=User):
    name = "User"
    name_plural = "Users"
    column_list = [User.tg_id, User.username]
    column_details_list = [User.tg_id, User.username]


class VPNAdmin(ModelView, model=UserVPN):
    name = "UserVPN"
    name_plural = "UserVPN"
    column_list = [UserVPN.id, UserVPN.view]


class PriceAdmin(ModelView, model=VPN):
    name = "VPN"
    name_plural = "VPN"
    column_list = [VPN.id, VPN.key_country, VPN.country_view_text]


class UserVPNAdmin(ModelView, model=Price):
    name = "Price"
    name_plural = "Price"
    column_list = [Price.id, Price.price, Price.price_view_text, Price.key_price]


admin.add_view(UserAdmin)
admin.add_view(VPNAdmin)
admin.add_view(PriceAdmin)
admin.add_view(UserVPNAdmin)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        reload=True,
    )
