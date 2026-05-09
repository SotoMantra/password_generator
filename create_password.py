import secrets
import string

def generate_password(length):
    length = int(input("How long this password should be?"))
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = "".join(secrets.choice(alphabet) for i in range(length))
    return password

print(generate_password(10))