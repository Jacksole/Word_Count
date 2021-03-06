"""empty message

Revision ID: d71aa69a98b3
Revises: None
Create Date: 2019-06-20 11:07:27.295361

"""

# revision identifiers, used by Alembic.
revision = 'd71aa69a98b3'
down_revision = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('results', sa.Column('result_all', postgresql.JSON(astext_type=sa.Text()), nullable=True))
    op.add_column('results', sa.Column('result_no_stop_words', postgresql.JSON(astext_type=sa.Text()), nullable=True))
    op.alter_column('results', 'url',
               existing_type=sa.TEXT(),
               nullable=True)
    op.drop_column('results', 'results_all')
    op.drop_column('results', 'results_no_stops_words')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('results', sa.Column('results_no_stops_words', postgresql.JSON(astext_type=sa.Text()), autoincrement=False, nullable=False))
    op.add_column('results', sa.Column('results_all', postgresql.JSON(astext_type=sa.Text()), autoincrement=False, nullable=False))
    op.alter_column('results', 'url',
               existing_type=sa.TEXT(),
               nullable=False)
    op.drop_column('results', 'result_no_stop_words')
    op.drop_column('results', 'result_all')
    # ### end Alembic commands ###
