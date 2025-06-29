"""Moving is_active

Revision ID: 763b581280cf
Revises: 6b41f5095d53
Create Date: 2025-06-13 01:23:34.549270

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '763b581280cf'
down_revision: Union[str, None] = '6b41f5095d53'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('profiles', 'is_active')
    op.add_column('users', sa.Column('is_active', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'is_active')
    op.add_column('profiles', sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
