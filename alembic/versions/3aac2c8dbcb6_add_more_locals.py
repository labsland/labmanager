"""Add more locals

Revision ID: 3aac2c8dbcb6
Revises: 56d38b1172f9
Create Date: 2017-06-09 19:35:21.477009

"""

# revision identifiers, used by Alembic.
revision = '3aac2c8dbcb6'
down_revision = '56d38b1172f9'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('UseLogs', sa.Column('local_datetime', sa.DateTime(), nullable=False))
    op.add_column('UseLogs', sa.Column('local_timezone', sa.Integer(), nullable=False))
    op.create_index(u'ix_UseLogs_local_datetime', 'UseLogs', ['local_datetime'], unique=False)
    op.create_index(u'ix_UseLogs_local_timezone', 'UseLogs', ['local_timezone'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(u'ix_UseLogs_local_timezone', table_name='UseLogs')
    op.drop_index(u'ix_UseLogs_local_datetime', table_name='UseLogs')
    op.drop_column('UseLogs', 'local_timezone')
    op.drop_column('UseLogs', 'local_datetime')
    ### end Alembic commands ###
