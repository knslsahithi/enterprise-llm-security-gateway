from services.prompt_injection_service import detect_prompt_injection

prompt = "What is Python programming?"

result = detect_prompt_injection(prompt)

print(result)