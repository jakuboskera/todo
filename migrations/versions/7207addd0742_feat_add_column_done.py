"""feat: add column done

Revision ID: 7207addd0742
Revises: 5c77959b8455
Create Date: 2023-02-21 16:48:03.468630

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7207addd0742'
down_revision = '5c77959b8455'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tasks', sa.Column('is_done', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tasks', 'is_done')
    # ### end Alembic commands ###