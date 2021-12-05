"""empty message

Revision ID: 559b4bb650bf
Revises: f0d11d2855a0
Create Date: 2021-12-05 13:56:31.907328

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '559b4bb650bf'
down_revision = 'f0d11d2855a0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('is_active', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'is_active')
    # ### end Alembic commands ###
