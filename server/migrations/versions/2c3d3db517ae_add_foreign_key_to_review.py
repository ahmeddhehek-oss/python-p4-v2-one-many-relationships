"""add foreign key to Review

Revision ID: 2c3d3db517ae
Revises: 3267fa24afbe
Create Date: 2026-01-04 14:02:09.723888

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2c3d3db517ae'
down_revision = '3267fa24afbe'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('reviews', schema=None) as batch_op:
        batch_op.create_foreign_key(
            batch_op.f('fk_reviews_employee_id_employees'),
            'employees',
            ['employee_id'],
            ['id']
        )

def downgrade():
    with op.batch_alter_table('reviews', schema=None) as batch_op:
        batch_op.drop_constraint(
            batch_op.f('fk_reviews_employee_id_employees'),
            type_='foreignkey'
        )


    # ### end Alembic commands ###
