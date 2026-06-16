import psycopg
import sys
from core.config import settings

def create_db():
    conn_str = f"postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_SERVER}:{settings.POSTGRES_PORT}/postgres"
    print(f"Connecting to postgres...")
    try:
        with psycopg.connect(conn_str, autocommit=True) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT 1 FROM pg_database WHERE datname='proposal_engine_db'")
                exists = cur.fetchone()
                if not exists:
                    cur.execute("CREATE DATABASE proposal_engine_db")
                    print("Created database proposal_engine_db")
                else:
                    print("Database already exists.")
    except Exception as e:
        print(f"Failed to create db: {e}")
        sys.exit(1)

if __name__ == "__main__":
    create_db()
