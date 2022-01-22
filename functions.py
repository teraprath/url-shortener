import random
import string

def new():
    list_digits = list(string.digits)
    list_alphabets = list(string.ascii_letters)
    password = ""
    password_chars = []
    chars = []
    chars += list_digits
    chars += list_alphabets

    for i in range(7):
        password_chars.append(random.choice(chars))

    random.shuffle(password_chars)

    for char in password_chars:
        password += char

    return password