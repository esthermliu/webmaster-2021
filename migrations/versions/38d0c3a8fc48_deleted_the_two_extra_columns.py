"""deleted the two extra columns

Revision ID: 38d0c3a8fc48
Revises: 81a15636a015
Create Date: 2021-02-23 20:42:03.791079

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '38d0c3a8fc48'
down_revision = '81a15636a015'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('appointments', schema=None) as batch_op:
        batch_op.drop_index('ix_appointments_complaint')
        batch_op.drop_index('ix_appointments_visit_type')
        batch_op.drop_column('complaint')
        batch_op.drop_column('visit_type')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('appointments', schema=None) as batch_op:
        batch_op.add_column(sa.Column('visit_type', sa.INTEGER(), nullable=True))
        batch_op.add_column(sa.Column('complaint', sa.INTEGER(), nullable=True))
        batch_op.create_index('ix_appointments_visit_type', ['visit_type'], unique=False)
        batch_op.create_index('ix_appointments_complaint', ['complaint'], unique=False)

    # ### end Alembic commands ###
