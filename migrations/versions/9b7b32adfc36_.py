"""empty message

Revision ID: 9b7b32adfc36
Revises: a7f988c03cb8
Create Date: 2018-07-15 17:00:33.020267

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9b7b32adfc36'
down_revision = 'a7f988c03cb8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('author', sa.String(length=255), nullable=True))
    op.add_column('posts', sa.Column('post_timestamp', sa.DateTime(), nullable=True))
    op.create_index(op.f('ix_posts_author'), 'posts', ['author'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_posts_author'), table_name='posts')
    op.drop_column('posts', 'post_timestamp')
    op.drop_column('posts', 'author')
    # ### end Alembic commands ###