def detect_prompt_injection(prompt):

    suspicious_patterns = [

        "ignore previous instructions",
        "forget all previous instructions",
        "bypass security",
        "act as a hacker",
        "system prompt",
        "reveal secrets",
        "disable safety",
        "ignore security policies"

    ]

    prompt_lower = prompt.lower()

    for pattern in suspicious_patterns:

        if pattern in prompt_lower:
            return True

    return False