"""empty message

Revision ID: 28d10699be99
Revises: 6326f6d484f5
Create Date: 2020-03-05 07:46:35.303036

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '28d10699be99'
down_revision = '6326f6d484f5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('phone', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'phone')
    # ### end Alembic commands ###
