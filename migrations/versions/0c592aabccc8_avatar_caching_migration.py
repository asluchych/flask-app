"""avatar caching migration

Revision ID: 0c592aabccc8
Revises: a537cadbb0e9
Create Date: 2022-11-19 11:08:44.578188

"""

# revision identifiers, used by Alembic.
revision = '0c592aabccc8'
down_revision = 'a537cadbb0e9'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('avatar_hash', sa.String(length=32), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'avatar_hash')
    # ### end Alembic commands ###