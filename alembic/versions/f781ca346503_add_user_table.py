"""add user table

Revision ID: f781ca346503
Revises: 51fc55864ce7
Create Date: 2022-08-16 00:50:15.354019

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f781ca346503'
down_revision = '51fc55864ce7'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable = False),
                    sa.Column('email', sa.Integer(), nullable = False),
                    sa.Column('password', sa.Integer(), nullable = False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone = True),server_default = sa.text('now()'), nullable = False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade():
    op.drop_table('users')
    pass
