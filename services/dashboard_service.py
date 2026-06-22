from sqlalchemy import text
from database.db_connection import engine

def get_audit_statistics():

    with engine.connect() as connection:

        total_requests = connection.execute(
            text("SELECT COUNT(*) FROM audit_logs")
        ).scalar()

        allowed_requests = connection.execute(
            text("SELECT COUNT(*) FROM audit_logs WHERE status='ALLOWED'")
        ).scalar()

        blocked_requests = connection.execute(
            text("SELECT COUNT(*) FROM audit_logs WHERE status!='ALLOWED'")
        ).scalar()

    return {
        "total_requests": total_requests,
        "allowed_requests": allowed_requests,
        "blocked_requests": blocked_requests
    }