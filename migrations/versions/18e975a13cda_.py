"""empty message

Revision ID: 18e975a13cda
Revises: 486897bdf04a
Create Date: 2023-04-10 16:45:33.733901

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '18e975a13cda'
down_revision = '486897bdf04a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('operacao', sa.Column('conta_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'operacao', 'conta', ['conta_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'operacao', type_='foreignkey')
    op.drop_column('operacao', 'conta_id')
    # ### end Alembic commands ###