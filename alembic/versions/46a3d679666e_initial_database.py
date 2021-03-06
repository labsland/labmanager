"""Initial database

Revision ID: 46a3d679666e
Revises: None
Create Date: 2013-10-08 01:34:51.501561

"""

# revision identifiers, used by Alembic.
revision = '46a3d679666e'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('rlmss',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('kind', sa.Unicode(length=50), nullable=False),
    sa.Column('location', sa.Unicode(length=50), nullable=False),
    sa.Column('url', sa.Unicode(length=300), nullable=False),
    sa.Column('version', sa.Unicode(length=50), nullable=False),
    sa.Column('configuration', sa.Unicode(length=10240), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('learning_tools',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Unicode(length=50), nullable=False),
    sa.Column('full_name', sa.Unicode(length=50), nullable=False),
    sa.Column('url', sa.Unicode(length=300), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('full_name'),
    sa.UniqueConstraint('name')
    )
    op.create_table('labmanager_users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('login', sa.Unicode(length=50), nullable=True),
    sa.Column('name', sa.Unicode(length=50), nullable=False),
    sa.Column('password', sa.Unicode(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('login')
    )
    op.create_table('lt_users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('login', sa.Unicode(length=50), nullable=False),
    sa.Column('full_name', sa.Unicode(length=50), nullable=False),
    sa.Column('password', sa.Unicode(length=128), nullable=False),
    sa.Column('access_level', sa.Unicode(length=50), nullable=False),
    sa.Column('lt_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['lt_id'], ['learning_tools.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('login','lt_id')
    )
    op.create_table('basic_http_credentials',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('lt_id', sa.Integer(), nullable=False),
    sa.Column('lt_login', sa.Unicode(length=50), nullable=False),
    sa.Column('lt_password', sa.Unicode(length=50), nullable=False),
    sa.Column('lt_url', sa.Unicode(length=300), nullable=True),
    sa.Column('labmanager_login', sa.Unicode(length=50), nullable=True),
    sa.Column('labmanager_password', sa.Unicode(length=50), nullable=True),
    sa.ForeignKeyConstraint(['lt_id'], ['learning_tools.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('lt_id'),
    sa.UniqueConstraint('lt_login')
    )
    op.create_table('laboratories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Unicode(length=50), nullable=False),
    sa.Column('laboratory_id', sa.Unicode(length=50), nullable=False),
    sa.Column('rlms_id', sa.Integer(), nullable=False),
    sa.Column('visibility', sa.Unicode(length=50), nullable=False),
    sa.Column('available', sa.Boolean(), nullable=False),
    sa.Column('default_local_identifier', sa.Unicode(length=50), nullable=False),
    sa.ForeignKeyConstraint(['rlms_id'], ['rlmss.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('laboratory_id','rlms_id')
    )
    op.create_table('courses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('lt_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Unicode(length=50), nullable=False),
    sa.Column('context_id', sa.Unicode(length=50), nullable=False),
    sa.ForeignKeyConstraint(['lt_id'], ['learning_tools.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('lt_id','context_id')
    )
    op.create_table('shindig_credentials',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('lt_id', sa.Integer(), nullable=False),
    sa.Column('shindig_url', sa.Unicode(length=50), nullable=False),
    sa.ForeignKeyConstraint(['lt_id'], ['learning_tools.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('lt_id')
    )
    op.create_table('request_permissions_lt',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('local_identifier', sa.Unicode(length=100), nullable=False),
    sa.Column('laboratory_id', sa.Integer(), nullable=False),
    sa.Column('lt_id', sa.Integer(), nullable=False),
    sa.Column('configuration', sa.Unicode(length=10240), nullable=True),
    sa.Column('accessible', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['laboratory_id'], ['laboratories.id'], ),
    sa.ForeignKeyConstraint(['lt_id'], ['learning_tools.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('laboratory_id','lt_id'),
    sa.UniqueConstraint('local_identifier','lt_id')
    )
    op.create_table('users2courses',
    sa.Column('course_id', sa.Integer(), nullable=True),
    sa.Column('lt_user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['course_id'], ['courses.id'], ),
    sa.ForeignKeyConstraint(['lt_user_id'], ['lt_users.id'], ),
    sa.PrimaryKeyConstraint()
    )
    op.create_table('permissions2lt',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('local_identifier', sa.Unicode(length=100), nullable=False),
    sa.Column('laboratory_id', sa.Integer(), nullable=False),
    sa.Column('lt_id', sa.Integer(), nullable=False),
    sa.Column('configuration', sa.Unicode(length=10240), nullable=True),
    sa.Column('accessible', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['laboratory_id'], ['laboratories.id'], ),
    sa.ForeignKeyConstraint(['lt_id'], ['learning_tools.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('laboratory_id','lt_id'),
    sa.UniqueConstraint('local_identifier','lt_id')
    )
    op.create_table('permissions2course',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('configuration', sa.Unicode(length=10240), nullable=True),
    sa.Column('permission_to_lt_id', sa.Integer(), nullable=False),
    sa.Column('course_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['course_id'], ['courses.id'], ),
    sa.ForeignKeyConstraint(['permission_to_lt_id'], ['permissions2lt.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('permission_to_lt_id','course_id')
    )
    op.create_table('permissions2ltuser',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('permission_to_lt_id', sa.Integer(), nullable=False),
    sa.Column('lt_user_id', sa.Integer(), nullable=False),
    sa.Column('key', sa.Unicode(length=100), nullable=False),
    sa.Column('secret', sa.Unicode(length=100), nullable=False),
    sa.ForeignKeyConstraint(['lt_user_id'], ['lt_users.id'], ),
    sa.ForeignKeyConstraint(['permission_to_lt_id'], ['permissions2lt.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('key'),
    sa.UniqueConstraint('permission_to_lt_id','lt_user_id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('permissions2ltuser')
    op.drop_table('permissions2course')
    op.drop_table('permissions2lt')
    op.drop_table('users2courses')
    op.drop_table('request_permissions_lt')
    op.drop_table('shindig_credentials')
    op.drop_table('courses')
    op.drop_table('laboratories')
    op.drop_table('basic_http_credentials')
    op.drop_table('lt_users')
    op.drop_table('labmanager_users')
    op.drop_table('learning_tools')
    op.drop_table('rlmss')
    ### end Alembic commands ###
