def detect_sql_injection(prompt):

    suspicious_patterns = [

        "' OR 1=1",
        "DROP TABLE",
        "DELETE FROM",
        "UNION SELECT",
        "INSERT INTO",
        "UPDATE SET",
        "--",
        ";"

    ]

    prompt_upper = prompt.upper()

    for pattern in suspicious_patterns:

        if pattern.upper() in prompt_upper:
            return True

    return False