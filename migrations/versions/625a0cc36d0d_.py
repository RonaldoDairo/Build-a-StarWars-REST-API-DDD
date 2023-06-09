"""empty message

Revision ID: 625a0cc36d0d
Revises: e720af284ac7
Create Date: 2023-04-12 21:19:16.428781

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '625a0cc36d0d'
down_revision = 'e720af284ac7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favorites', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('user_id_people',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('user_id_planets',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('user_id_vehicles',
               existing_type=sa.INTEGER(),
               nullable=True)

    with op.batch_alter_table('people', schema=None) as batch_op:
        batch_op.add_column(sa.Column('planets_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'planets', ['planets_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('people', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('planets_id')

    with op.batch_alter_table('favorites', schema=None) as batch_op:
        batch_op.alter_column('user_id_vehicles',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('user_id_planets',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('user_id_people',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###
