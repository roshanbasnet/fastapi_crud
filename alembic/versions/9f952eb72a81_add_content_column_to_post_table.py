"""add content column to post table 

Revision ID: 9f952eb72a81
Revises: c597fe80fa7c
Create Date: 2022-12-29 10:31:51.035551

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9f952eb72a81'
down_revision = 'c597fe80fa7c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts1", sa.Column('content', sa.String, nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts1", "content")
    pass
