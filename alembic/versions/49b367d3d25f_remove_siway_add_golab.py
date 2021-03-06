"""Remove SiWay, add GoLab

Revision ID: 49b367d3d25f
Revises: 13f9fd64f85b
Create Date: 2017-04-07 01:07:29.653200

"""

# revision identifiers, used by Alembic.
revision = '49b367d3d25f'
down_revision = '13f9fd64f85b'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('GoLabOAuthUsers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('display_name', sa.Unicode(length=255), nullable=False),
    sa.Column('email', sa.Unicode(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(u'ix_GoLabOAuthUsers_display_name', 'GoLabOAuthUsers', ['display_name'], unique=False)
    op.create_index(u'ix_GoLabOAuthUsers_email', 'GoLabOAuthUsers', ['email'], unique=True)
    op.drop_constraint(u'EmbedApplications_ibfk_1', 'EmbedApplications', type_='foreignkey')
    op.drop_column('EmbedApplications', u'owner_id')
    try:
        op.drop_table(u'siway_user')
    except:
        pass
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('EmbedApplications', sa.Column(u'owner_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.create_foreign_key(u'EmbedApplications_ibfk_1', u'EmbedApplications', u'siway_user', [u'owner_id'], [u'id'])
    op.create_table(u'siway_user',
    sa.Column(u'id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column(u'email', mysql.VARCHAR(length=255), nullable=False),
    sa.Column(u'uid', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column(u'employee_type', mysql.VARCHAR(length=255), nullable=False),
    sa.Column(u'full_name', mysql.VARCHAR(length=255), nullable=False),
    sa.Column(u'short_name', mysql.VARCHAR(length=255), nullable=False),
    sa.Column(u'school_name', mysql.VARCHAR(length=255), nullable=False),
    sa.Column(u'group', mysql.VARCHAR(length=255), nullable=False),
    sa.PrimaryKeyConstraint(u'id'),
    mysql_default_charset=u'latin1',
    mysql_engine=u'InnoDB'
    )
    op.drop_index(u'ix_GoLabOAuthUsers_email', table_name='GoLabOAuthUsers')
    op.drop_index(u'ix_GoLabOAuthUsers_display_name', table_name='GoLabOAuthUsers')
    op.drop_table('GoLabOAuthUsers')
    ### end Alembic commands ###
