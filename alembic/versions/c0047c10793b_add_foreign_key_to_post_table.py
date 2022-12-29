"""add foreign key to post table

Revision ID: c0047c10793b
Revises: 7d8fc80bf2c3
Create Date: 2022-12-29 11:43:57.907662

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c0047c10793b'
down_revision = '7d8fc80bf2c3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column('owner_id', sa.Integer()), nullable=False)
    op.create_foreign_key("post_users_fk", source_table="posts", referent_table="users", local_cols=[
                          "owner_id"], remote_cols=["id"], ondelete="CASCADE")
    pass


def downgrade() -> None:
    pass
