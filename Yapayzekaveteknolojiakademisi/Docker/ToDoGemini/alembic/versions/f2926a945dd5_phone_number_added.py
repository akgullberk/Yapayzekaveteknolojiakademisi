"""phone number added

Revision ID: f2926a945dd5
Revises: 
Create Date: 2025-02-11 12:09:19.711441

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f2926a945dd5'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("users",sa.Column("phone_number", sa.String(20), nullable=True))


def downgrade() -> None:
    op.drop_column("users", "phone_number")
