"""Add gedung and lantai columns to fasilitas

Revision ID: 3a78fa33eede
Revises: be4ee28ee050
Create Date: 2024-12-05 09:27:52.740485

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3a78fa33eede'
down_revision = 'be4ee28ee050'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('fasilitas', schema=None) as batch_op:
        batch_op.add_column(sa.Column('gedung', sa.String(length=100), nullable=True))
        batch_op.add_column(sa.Column('lantai', sa.String(length=100), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('fasilitas', schema=None) as batch_op:
        batch_op.drop_column('lantai')
        batch_op.drop_column('gedung')

    # ### end Alembic commands ###
