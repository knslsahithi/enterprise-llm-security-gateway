from services.pii_service import redact_pii
from services.custom_redaction_service import redact_custom_data

def sanitize_prompt(text):

    text = redact_pii(text)

    text = redact_custom_data(text)

    return text