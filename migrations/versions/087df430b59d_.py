"""empty message

Revision ID: 087df430b59d
Revises: 8d2afdd1b35b
Create Date: 2018-07-15 16:42:51.990034

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '087df430b59d'
down_revision = '8d2afdd1b35b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'draft')
    op.drop_column('posts', 'view_num')
    op.drop_column('posts', 'edit_timestamp')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('edit_timestamp', mysql.DATETIME(), nullable=True))
    op.add_column('posts', sa.Column('view_num', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.add_column('posts', sa.Column('draft', mysql.TEXT(), nullable=True))
    # ### end Alembic commands ###
