"""add key_price, key_country field in user_vpn, change column name country > key_country in vpn

Revision ID: 9c7063ccb0ed
Revises: d645eb10f9e1
Create Date: 2024-10-26 13:10:10.326979

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "9c7063ccb0ed"
down_revision: Union[str, None] = "d645eb10f9e1"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "user_vpn",
        sa.Column("key_country", sa.String(length=255), nullable=False),
    )
    op.add_column(
        "user_vpn",
        sa.Column("key_price", sa.String(length=255), nullable=False),
    )
    op.add_column(
        "vpn", sa.Column("key_country", sa.String(length=255), nullable=False)
    )
    op.drop_column("vpn", "country")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "vpn",
        sa.Column(
            "country",
            sa.VARCHAR(length=255),
            autoincrement=False,
            nullable=False,
        ),
    )
    op.drop_column("vpn", "key_country")
    op.drop_column("user_vpn", "key_price")
    op.drop_column("user_vpn", "key_country")
    # ### end Alembic commands ###