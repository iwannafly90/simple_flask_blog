"""empty message

Revision ID: 21b65f770cbb
Revises: 7abe49aab515
Create Date: 2019-10-25 23:16:38.174394

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '21b65f770cbb'
down_revision = '7abe49aab515'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post_tags',
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.Column('tag_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tag.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post_tags')
    # ### end Alembic commands ###
