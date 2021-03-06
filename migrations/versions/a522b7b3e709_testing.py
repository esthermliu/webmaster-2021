"""testing

Revision ID: a522b7b3e709
Revises: 7e249765204c
Create Date: 2021-03-07 18:27:43.962236

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a522b7b3e709'
down_revision = '7e249765204c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('address')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('address', sa.INTEGER(), nullable=True))

    # ### end Alembic commands ###
