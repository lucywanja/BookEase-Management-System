"""Initial migration.

Revision ID: 4fd3f94959d7
Revises: 
Create Date: 2024-09-04 19:02:25.596203

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4fd3f94959d7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('books',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('author', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('members',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('borrow_records',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('borrow_date', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('return_date', sa.DateTime(), nullable=True),
    sa.Column('condition_on_return', sa.String(), nullable=True),
    sa.Column('member_id', sa.Integer(), nullable=True),
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['book_id'], ['books.id'], name=op.f('fk_borrow_records_book_id_books')),
    sa.ForeignKeyConstraint(['member_id'], ['members.id'], name=op.f('fk_borrow_records_member_id_members')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('borrow_records')
    op.drop_table('members')
    op.drop_table('books')
    # ### end Alembic commands ###
