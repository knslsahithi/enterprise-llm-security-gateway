from services.db_log_service import save_log

save_log(
    "emp001",
    "Testing PostgreSQL Logging",
    "ALLOWED"
)

print("Log Inserted Successfully")