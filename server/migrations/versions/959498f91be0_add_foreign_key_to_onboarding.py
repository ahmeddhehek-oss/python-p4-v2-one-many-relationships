"""add foreign key to onboarding

Revision ID: 959498f91be0
Revises: 2c3d3db517ae
Create Date: 2026-01-04 14:55:07.065802

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '959498f91be0'
down_revision = '2c3d3db517ae'
branch_labels = None
depends_on = None


def upgrade():
    # Use batch_alter_table for SQLite
    with op.batch_alter_table('onboardings', schema=None) as batch_op:
        # Do NOT re-add the column, it's already in the model
        batch_op.create_foreign_key(
            batch_op.f('fk_onboardings_employee_id_employees'),
            'employees',
            ['employee_id'],
            ['id']
        )

def downgrade():
    with op.batch_alter_table('onboardings', schema=None) as batch_op:
        batch_op.drop_constraint(
            batch_op.f('fk_onboardings_employee_id_employees'),
            type_='foreignkey'
        )
