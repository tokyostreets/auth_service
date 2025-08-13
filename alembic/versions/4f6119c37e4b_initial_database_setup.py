"""Initial database setup

Revision ID: 4f6119c37e4b
Revises: 
Create Date: 2025-08-13 18:34:35.690746

"""
from alembic import op
import sqlalchemy as sa

revision = '4f6119c37e4b'
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.execute("""
    CREATE EXTENSION IF NOT EXISTS pgcrypto;
    
    CREATE TABLE users (
        id SERIAL PRIMARY KEY,
        email VARCHAR NOT NULL UNIQUE,
        password VARCHAR NOT NULL,
        is_active BOOLEAN DEFAULT TRUE NOT NULL
    );
    
    CREATE INDEX ix_users_email ON users (email);
    CREATE INDEX ix_users_id ON users (id);
    """)

def downgrade() -> None:
    op.execute("""
    DROP TABLE users;
    DROP EXTENSION pgcrypto;
    """)