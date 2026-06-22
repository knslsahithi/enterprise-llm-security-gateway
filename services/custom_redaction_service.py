import re

def redact_custom_data(text):

    text = re.sub(
        r"EMP\d+",
        "<EMPLOYEE_ID>",
        text
    )

    text = re.sub(
        r"PRJ-[A-Z]+-\d+",
        "<PROJECT_CODE>",
        text
    )

    return text