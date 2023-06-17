import random
import string

from test_app.settings import LOGIN_LEN


def generate_login():
    letters = string.ascii_letters
    return "".join(random.choice(letters) for _ in range(LOGIN_LEN))
