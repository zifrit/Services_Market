"""add balance in users table

Revision ID: 2a78e522f406
Revises: 38d167205a9c
Create Date: 2024-10-24 12:59:53.739805

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "2a78e522f406"
down_revision: Union[str, None] = "38d167205a9c"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, "referral", ["id"])
    op.add_column(
        "users",
        sa.Column("balance", sa.Integer(), server_default="0", nullable=False),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("users", "balance")
    op.drop_constraint(None, "referral", type_="unique")
    # ### end Alembic commands ###