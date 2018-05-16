"""
Migration script for workflow request tables.
"""
from __future__ import print_function

import logging

from sqlalchemy import Column, ForeignKey, Integer, MetaData, TEXT, Table, Unicode

from galaxy.model.custom_types import JSONType

log = logging.getLogger(__name__)
metadata = MetaData()


WorkflowStepInput_table = Table(
    "workflow_step_input", metadata,
    Column("id", Integer, primary_key=True),
    Column("workflow_step_id", Integer, ForeignKey("workflow_step.id"), index=True),
    Column("name", Unicode(255)),
    Column("merge_type", TEXT),
    Column("scatter_type", TEXT),
    Column("value_from", JSONType),
    Column("value_from_type", TEXT),
    Column("default_value", JSONType),
)


TABLES = [
    WorkflowStepInput_table,
]


def upgrade(migrate_engine):
    metadata.bind = migrate_engine
    print(__doc__)
    metadata.reflect()

    for table in TABLES:
        __create(table)


def downgrade(migrate_engine):
    metadata.bind = migrate_engine
    metadata.reflect()

    for table in TABLES:
        __drop(table)


def __create(table):
    try:
        table.create()
    except Exception:
        log.exception("Creating %s table failed.", table.name)


def __drop(table):
    try:
        table.drop()
    except Exception:
        log.exception("Dropping %s table failed.", table.name)
