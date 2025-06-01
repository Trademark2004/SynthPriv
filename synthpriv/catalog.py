# synthpriv/catalog.py
import os
import json
import hashlib
import pandas as pd
from dotenv import load_dotenv  # For .env support
import psycopg2  # PostgreSQL support

# Load environment variables from .env if present
load_dotenv()
DSN = os.getenv('POSTGRES_DSN')  # Optional Postgres DSN
CATALOG_JSON = 'catalog.json'  # Fallback JSON catalog

# Helper: Hash file contents for versioning
def _hash_path(path):
    with open(path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()

# Add a dataset to the catalog (Postgres or JSON)
def catalog_add(path):
    version = _hash_path(path)
    if DSN:
        # Store in Postgres
        conn = psycopg2.connect(DSN)
        cur = conn.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS catalog (id TEXT, path TEXT, version TEXT)')
        cur.execute('INSERT INTO catalog VALUES (%s, %s, %s)', (os.path.basename(path), path, version))
        conn.commit()
        cur.close()
        conn.close()
    else:
        # Store in local JSON
        if os.path.exists(CATALOG_JSON):
            with open(CATALOG_JSON) as f:
                data = json.load(f)
        else:
            data = []
        data.append({'id': os.path.basename(path), 'path': path, 'version': version})
        with open(CATALOG_JSON, 'w') as f:
            json.dump(data, f, indent=2)

# List all datasets in the catalog
def catalog_list():
    if DSN:
        conn = psycopg2.connect(DSN)
        cur = conn.cursor()
        cur.execute('SELECT * FROM catalog')
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return rows
    else:
        if os.path.exists(CATALOG_JSON):
            with open(CATALOG_JSON) as f:
                return json.load(f)
        return []
