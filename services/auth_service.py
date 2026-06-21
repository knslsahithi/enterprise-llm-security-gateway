AUTHORIZED_USERS = [
    "emp001",
    "emp002",
    "emp003",
    "security_admin"
]

def authenticate_user(username: str):
    return username.lower() in AUTHORIZED_USERS