user_roles = {
    "emp001": "ENGINEERING",
    "emp002": "HR",
    "emp003": "FINANCE"
}

role_permissions = {
    "ENGINEERING": ["GPT4", "CLAUDE"],
    "HR": ["HR_BOT"],
    "FINANCE": ["FINANCE_BOT"]
}

def check_access(username, model):

    role = user_roles.get(username)

    if not role:
        return False

    return model in role_permissions.get(role, [])