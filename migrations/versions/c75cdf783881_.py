"""empty message

Revision ID: c75cdf783881
Revises: 75fc3c1f3fd2
Create Date: 2023-04-01 22:51:30.390982

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c75cdf783881'
down_revision = '75fc3c1f3fd2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('people', schema=None) as batch_op:
        batch_op.add_column(sa.Column('username', sa.String(length=150), nullable=False))
        batch_op.add_column(sa.Column('description', sa.String(length=200), nullable=False))
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=True))
        batch_op.drop_constraint('people_username_person_key', type_='unique')
        batch_op.create_unique_constraint(None, ['username'])
        batch_op.create_foreign_key(None, 'user', ['user_id'], ['id'])
        batch_op.drop_column('username_person')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('people', schema=None) as batch_op:
        batch_op.add_column(sa.Column('username_person', sa.VARCHAR(length=40), autoincrement=False, nullable=False))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='unique')
        batch_op.create_unique_constraint('people_username_person_key', ['username_person'])
        batch_op.drop_column('user_id')
        batch_op.drop_column('description')
        batch_op.drop_column('username')

    # ### end Alembic commands ###
