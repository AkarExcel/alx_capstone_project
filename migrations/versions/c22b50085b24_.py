"""empty message

Revision ID: c22b50085b24
Revises: 
Create Date: 2023-10-13 19:15:21.700013

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c22b50085b24'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('portfolio',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=True),
    sa.Column('mainimage', sa.String(length=100), nullable=True),
    sa.Column('smallimage', sa.String(length=100), nullable=True),
    sa.Column('client', sa.String(length=100), nullable=True),
    sa.Column('role', sa.String(length=100), nullable=True),
    sa.Column('product', sa.String(length=100), nullable=True),
    sa.Column('durations', sa.String(length=100), nullable=True),
    sa.Column('tool', sa.String(length=100), nullable=True),
    sa.Column('link', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('portfolio')
    # ### end Alembic commands ###