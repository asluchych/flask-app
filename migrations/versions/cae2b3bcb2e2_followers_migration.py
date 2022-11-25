"""followers migration

Revision ID: cae2b3bcb2e2
Revises: 409d30ed3ea1
Create Date: 2022-11-25 11:58:56.853086

"""

# revision identifiers, used by Alembic.
revision = 'cae2b3bcb2e2'
down_revision = '409d30ed3ea1'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('follows',
    sa.Column('follower_id', sa.Integer(), nullable=False),
    sa.Column('followed_id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('follower_id', 'followed_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('follows')
    # ### end Alembic commands ###
