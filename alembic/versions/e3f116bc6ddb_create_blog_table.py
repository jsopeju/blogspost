"""create blog table

Revision ID: e3f116bc6ddb
Revises: 
Create Date: 2024-09-10 21:22:01.817419

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e3f116bc6ddb'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('Blogs', sa.Column('id', sa.Integer(), primary_key=True, nullable=False),
                            sa.Column('title', sa.String(), nullable=False),
                            sa.Column('content', sa.String(), nullable=False),
                            sa.Column('publised', sa.Boolean()))


    pass


def downgrade() -> None:
    op.drop_table('Blog')
    pass
