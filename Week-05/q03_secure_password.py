import random
def generate_password():
    uppercase_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase_chars = "abcdefghijklmnopqrstuvwxyz"
    digits = "0123456789"
    special_chars = "!@#$%^&*()-_=+[{]};:',<.>/?"
    password = [random.choice(uppercase_chars),random.choice(uppercase_chars),random.choice(digits),random.choice(special_chars)]
    all_chars = uppercase_chars + lowercase_chars + digits + special_chars
    for i in range(6):
        password.append(random.choice(all_chars))
    random.shuffle(password)
    return "".join(password)
print("Generated Password:", generate_password())
