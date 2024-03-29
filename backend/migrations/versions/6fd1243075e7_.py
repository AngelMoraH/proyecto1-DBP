"""empty message

Revision ID: 6fd1243075e7
Revises: 
Create Date: 2022-05-23 11:31:35.303402

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6fd1243075e7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('usuario', sa.Column('rol', sa.String(), nullable=True))
    op.execute("UPDATE usuario SET rol='default' WHERE rol IS NULL;")
    op.alter_column('usuario', 'rol', nullable=False)
    # ### end Alembic commands ###
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('usuario', 'rol')
    # ### end Alembic commands ###
