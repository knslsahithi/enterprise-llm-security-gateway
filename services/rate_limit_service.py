from datetime import datetime

user_requests = {}

MAX_REQUESTS = 3

def check_rate_limit(username):

    current_time = datetime.now()

    if username not in user_requests:
        user_requests[username] = []

    user_requests[username].append(current_time)

    if len(user_requests[username]) > MAX_REQUESTS:
        return False

    return True