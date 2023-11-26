# Random Key Gen by
# Richard Wadsworth

import string
import random

def generate_password(length):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_characters) for i in range(length))
    return password

if __name__ == "__main__":
    password_length = 10  # You can change this to the desired length
    password = generate_password(password_length)
    print(password)
