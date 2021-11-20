"""empty message

Revision ID: 18d5989fdd1b
Revises: b6abbf2c1ca1
Create Date: 2021-11-14 10:58:53.917189

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '18d5989fdd1b'
down_revision = 'b6abbf2c1ca1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('is_deleted', sa.Boolean(), nullable=True))
    op.add_column('user', sa.Column('is_blocked', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'is_blocked')
    op.drop_column('user', 'is_deleted')
    # ### end Alembic commands ###
