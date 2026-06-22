from services.pii_service import redact_pii

sample_text = """
My name is John.
My email is john@gmail.com
My credit card number is 4111-1111-1111-1111
"""

result = redact_pii(sample_text)

print(result)