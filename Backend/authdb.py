#!/usr/bin/env python3
"""
Initialize the database if it doesn't exist.
This script ensures the SQLite database is created with the proper schema.
"""

import os
import sqlite3

# Ensure data directory exists
os.makedirs("data", exist_ok=True)

# Check if database exists
db_path = "data/local.db"
db_exists = os.path.exists(db_path)

if not db_exists:
    print(f"Database not found at {db_path}. Creating...")
    
    # Read and execute init.sql
    with open("init.sql", "r") as f:
        init_script = f.read()
    
    conn = sqlite3.connect(db_path)
    try:
        conn.executescript(init_script)
        conn.commit()
        print(f"Database created successfully at {db_path}")
    except Exception as e:
        print(f"Error creating database: {e}")
        raise
    finally:
        conn.close()
else:
    print(f"Database already exists at {db_path}")
