"""empty message

Revision ID: 75920e4b5d05
Revises: 6cd6affd94a5
Create Date: 2022-07-09 19:32:45.261756

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '75920e4b5d05'
down_revision = '6cd6affd94a5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('usuario', sa.Column('rol', sa.String(), nullable=True))
    op.execute("UPDATE usuario SET rol='default' WHERE rol IS NULL;")
    op.alter_column('usuario', 'rol', nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('usuario', 'rol')
    # ### end Alembic commands ###
