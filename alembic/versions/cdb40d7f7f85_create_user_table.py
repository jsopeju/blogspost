"""create user table

Revision ID: cdb40d7f7f85
Revises: e3f116bc6ddb
Create Date: 2024-09-10 21:35:02.309006

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cdb40d7f7f85'
down_revision: Union[str, None] = 'e3f116bc6ddb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('Users', sa.Column('id', sa.Integer(), primary_key=True, nullable=False),
                            sa.Column('name', sa.String(), nullable=False),
                            sa.Column('email', sa.String(), nullable=False),
                            sa.Column('password', sa.String(), nullable=False))

    pass


def downgrade() -> None:
    op.drop_table('Users')
    pass
