from datetime import datetime

def write_log(username, prompt, status):

    log_entry = (
        f"{datetime.now()} | "
        f"USER={username} | "
        f"PROMPT={prompt} | "
        f"STATUS={status}\n"
    )

    with open("logs/audit.log", "a") as file:
        file.write(log_entry)