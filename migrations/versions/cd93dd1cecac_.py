"""empty message

Revision ID: cd93dd1cecac
Revises: 
Create Date: 2022-05-13 17:37:35.152882

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'cd93dd1cecac'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comentarios')
    op.drop_table('likes')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('likes',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('data', postgresql.JSON(astext_type=sa.Text()), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='likes_pkey')
    )
    op.create_table('comentarios',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('data', postgresql.JSON(astext_type=sa.Text()), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='comentarios_pkey')
    )
    # ### end Alembic commands ###
