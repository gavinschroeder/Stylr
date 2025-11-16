#!/usr/bin/env python3
"""
Initialize the analytics database tables.
This script ensures the SQLAlchemy tables for Items and Interactions are created.
"""

import os

# Ensure data directory exists
os.makedirs("data", exist_ok=True)

from db import Base, engine
from Analytics.model_interactions import Item, Interaction

# Create all tables
print("Creating analytics database tables...")
Base.metadata.create_all(engine)
print("Analytics database tables created successfully!")
print(f"Database location: {engine.url}")

# Verify tables were created
from sqlalchemy import inspect
inspector = inspect(engine)
tables = inspector.get_table_names()
print(f"Tables in database: {tables}")
