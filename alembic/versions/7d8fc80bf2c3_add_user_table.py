"""add user table

Revision ID: 7d8fc80bf2c3
Revises: 9f952eb72a81
Create Date: 2022-12-29 10:35:15.172962

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7d8fc80bf2c3'
down_revision = '9f952eb72a81'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("users", sa.Column('id', sa.Integer, primary_key=True, nullable=False),
                    sa.Column('email', sa.String, nullable=False, unique=True),
                    sa.Column('password', sa.String, nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade() -> None:
    op.drop_table("users")
    pass
