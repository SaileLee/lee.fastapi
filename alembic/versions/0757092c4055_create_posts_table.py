"""create posts table

Revision ID: 0757092c4055
Revises: 
Create Date: 2022-08-16 00:24:53.300169

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0757092c4055'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable = False, primary_key = True), sa.Column('title', sa.String(), nullable = False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
