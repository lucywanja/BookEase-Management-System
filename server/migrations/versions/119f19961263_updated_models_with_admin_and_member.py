"""Updated models with Admin and Member

Revision ID: 119f19961263
Revises: ace3497eb37c
Create Date: 2024-09-04 23:10:48.377931

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '119f19961263'
down_revision = 'ace3497eb37c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admins',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=False),
    sa.Column('last_name', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_admins')),
    sa.UniqueConstraint('email', name=op.f('uq_admins_email'))
    )
    with op.batch_alter_table('books', schema=None) as batch_op:
        batch_op.add_column(sa.Column('admin_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(batch_op.f('fk_books_admin_id_admins'), 'admins', ['admin_id'], ['id'])

    with op.batch_alter_table('borrow_records', schema=None) as batch_op:
        batch_op.add_column(sa.Column('admin_id', sa.Integer(), nullable=True))
        batch_op.alter_column('return_date',
               existing_type=sa.DATETIME(),
               nullable=False)
        batch_op.alter_column('book_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('member_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.create_foreign_key(batch_op.f('fk_borrow_records_admin_id_admins'), 'admins', ['admin_id'], ['id'])

    with op.batch_alter_table('members', schema=None) as batch_op:
        batch_op.add_column(sa.Column('admin_id', sa.Integer(), nullable=True))
        batch_op.create_unique_constraint(batch_op.f('uq_members_email'), ['email'])
        batch_op.create_foreign_key(batch_op.f('fk_members_admin_id_admins'), 'admins', ['admin_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('members', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_members_admin_id_admins'), type_='foreignkey')
        batch_op.drop_constraint(batch_op.f('uq_members_email'), type_='unique')
        batch_op.drop_column('admin_id')

    with op.batch_alter_table('borrow_records', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_borrow_records_admin_id_admins'), type_='foreignkey')
        batch_op.alter_column('member_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('book_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('return_date',
               existing_type=sa.DATETIME(),
               nullable=True)
        batch_op.drop_column('admin_id')

    with op.batch_alter_table('books', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_books_admin_id_admins'), type_='foreignkey')
        batch_op.drop_column('admin_id')

    op.drop_table('admins')
    # ### end Alembic commands ###
