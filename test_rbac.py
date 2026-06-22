from services.rbac_service import check_access

print(check_access("emp001", "GPT4"))
print(check_access("emp002", "GPT4"))