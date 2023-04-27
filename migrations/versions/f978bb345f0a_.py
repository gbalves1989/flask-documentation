"""empty message

Revision ID: f978bb345f0a
Revises: b27d908a2cf2
Create Date: 2023-04-24 18:31:47.855149

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f978bb345f0a'
down_revision = 'b27d908a2cf2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('teacher_graduation',
    sa.Column('teacher_id', sa.Integer(), nullable=False),
    sa.Column('graduation_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['graduation_id'], ['graduation.id'], ),
    sa.ForeignKeyConstraint(['teacher_id'], ['teacher.id'], ),
    sa.PrimaryKeyConstraint('teacher_id', 'graduation_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('teacher_graduation')
    # ### end Alembic commands ###
