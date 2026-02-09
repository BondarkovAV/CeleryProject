"""initial schema

Revision ID: 912d3f5f7ad5
Revises: 
Create Date: 2026-02-09 21:38:35.475242

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '912d3f5f7ad5'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "user",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("email", sa.String(), unique=True, nullable=False),
    )


def downgrade() -> None:
    """Downgrade schema."""
    pass
