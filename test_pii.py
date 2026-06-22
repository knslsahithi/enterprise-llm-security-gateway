from services.pii_service import detect_pii

text = """
My name is John.
My email is john@gmail.com
My credit card is 4111-1111-1111-1111
"""

results = detect_pii(text)

for item in results:
    print(item)