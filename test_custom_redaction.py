from services.custom_redaction_service import redact_custom_data

sample_text = """
Employee ID: EMP12345
Project: PRJ-FEDX-2025
"""

result = redact_custom_data(sample_text)

print(result)