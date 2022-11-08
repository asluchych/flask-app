"""initial migration

Revision ID: 77f6d85045e9
Revises: 38c4e85512a9
Create Date: 2022-11-08 14:51:17.286899

"""

# revision identifiers, used by Alembic.
revision = '77f6d85045e9'
down_revision = '38c4e85512a9'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_hash', sa.String(length=128), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'password_hash')
    # ### end Alembic commands ###
