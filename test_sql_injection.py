from services.sql_injection_service import detect_sql_injection

prompt = "What is Python?"

result = detect_sql_injection(prompt)

print(result)