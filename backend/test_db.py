from sqlalchemy import text

from database.connection import engine


with engine.connect() as conn:
    result = conn.execute(
        text("SELECT current_database();")
    )

    print(result.fetchone())