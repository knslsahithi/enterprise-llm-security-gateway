from services.dlp_service import sanitize_prompt

sample_text = """
My name is John.
Email: john@gmail.com
Employee ID: EMP12345
Project: PRJ-FEDX-2025
Credit Card: 4111-1111-1111-1111
"""

result = sanitize_prompt(sample_text)

print(result)