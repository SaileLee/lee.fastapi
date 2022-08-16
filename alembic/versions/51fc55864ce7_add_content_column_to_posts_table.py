"""add content column to posts table

Revision ID: 51fc55864ce7
Revises: 0757092c4055
Create Date: 2022-08-16 00:39:43.424955

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '51fc55864ce7'
down_revision = '0757092c4055'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable = False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
