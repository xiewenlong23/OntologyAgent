"""initial schema

Revision ID: 72c3397a65e5
Revises:
Create Date: 2026-06-20 10:48:19.890830

"""
from typing import Sequence, Union

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from alembic import op


# revision identifiers, used by Alembic.
revision: str = "72c3397a65e5"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "ontologies",
        sa.Column("id", sa.String(length=36), primary_key=True),
        sa.Column("tenant_id", sa.String(length=36), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("version", sa.Integer(), nullable=False, server_default="1"),
        sa.Column("object_types", postgresql.JSONB, nullable=False, server_default="{}"),
        sa.Column("properties", postgresql.JSONB, nullable=False, server_default="{}"),
        sa.Column("link_types", postgresql.JSONB, nullable=False, server_default="{}"),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.text("now()")),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.text("now()")),
    )
    op.create_index("ix_ontologies_tenant_id", "ontologies", ["tenant_id"])

    op.create_table(
        "objects",
        sa.Column("id", sa.String(length=36), primary_key=True),
        sa.Column("tenant_id", sa.String(length=36), nullable=False),
        sa.Column("ontology_id", sa.String(length=36), sa.ForeignKey("ontologies.id"), nullable=False),
        sa.Column("object_type", sa.String(length=255), nullable=False),
        sa.Column("api_name", sa.String(length=255), nullable=False),
        sa.Column("display_name", sa.String(length=255), nullable=False),
        sa.Column("properties", postgresql.JSONB, nullable=False, server_default="{}"),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.text("now()")),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.text("now()")),
    )
    op.create_index("ix_objects_tenant_id", "objects", ["tenant_id"])
    op.create_index(
        "ix_objects_tenant_ontology_type",
        "objects",
        ["tenant_id", "ontology_id", "object_type"],
    )

    op.create_table(
        "object_links",
        sa.Column("id", sa.String(length=36), primary_key=True),
        sa.Column("tenant_id", sa.String(length=36), nullable=False),
        sa.Column("source_object_id", sa.String(length=36), sa.ForeignKey("objects.id"), nullable=False),
        sa.Column("target_object_id", sa.String(length=36), sa.ForeignKey("objects.id"), nullable=False),
        sa.Column("link_type", sa.String(length=255), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.text("now()")),
    )
    op.create_index("ix_object_links_tenant_id", "object_links", ["tenant_id"])


def downgrade() -> None:
    op.drop_index("ix_object_links_tenant_id", table_name="object_links")
    op.drop_table("object_links")
    op.drop_index("ix_objects_tenant_ontology_type", table_name="objects")
    op.drop_index("ix_objects_tenant_id", table_name="objects")
    op.drop_table("objects")
    op.drop_index("ix_ontologies_tenant_id", table_name="ontologies")
    op.drop_table("ontologies")
