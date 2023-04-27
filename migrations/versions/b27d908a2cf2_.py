"""empty message

Revision ID: b27d908a2cf2
Revises: 58a6e7c2ba81
Create Date: 2023-04-24 17:25:59.773625

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b27d908a2cf2'
down_revision = '58a6e7c2ba81'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('course', sa.Column('graduation_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'course', 'graduation', ['graduation_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'course', type_='foreignkey')
    op.drop_column('course', 'graduation_id')
    # ### end Alembic commands ###
