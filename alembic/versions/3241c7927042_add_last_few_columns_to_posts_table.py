"""add last few columns to posts table

Revision ID: 3241c7927042
Revises: 2670bec9a766
Create Date: 2022-08-16 01:24:09.325377

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3241c7927042'
down_revision = '2670bec9a766'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable = False, server_default = 'True'),)
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone = True), nullable = False, server_default = sa.text('Now()')),)
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
