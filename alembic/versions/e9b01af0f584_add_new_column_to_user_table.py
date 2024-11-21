"""Add new column to User table

Revision ID: e9b01af0f584
Revises: a2e652b7f5d1
Create Date: 2024-11-21 18:14:19.363029

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e9b01af0f584'
down_revision: Union[str, None] = 'a2e652b7f5d1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('todos', sa.VARCHAR(), nullable=True))
    op.add_column('todos', sa.Column('user_id', sa.VARCHAR(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('todos', 'user_id')
    op.drop_column('users', 'todos')
    # ### end Alembic commands ###