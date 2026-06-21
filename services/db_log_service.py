from sqlalchemy import text
from database.db_connection import engine

def save_log(username, prompt, status):

    with engine.connect() as connection:

        query = text("""
            INSERT INTO audit_logs
            (username, prompt, status)

            VALUES
            (:username, :prompt, :status)
        """)

        connection.execute(
            query,
            {
                "username": username,
                "prompt": prompt,
                "status": status
            }
        )

        connection.commit()