"""initial migration

Revision ID: 48c42d465f95
Revises: e3a683857d29
Create Date: 2022-11-11 18:00:01.639603

"""

# revision identifiers, used by Alembic.
revision = '48c42d465f95'
down_revision = 'e3a683857d29'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('confirmed', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'confirmed')
    # ### end Alembic commands ###