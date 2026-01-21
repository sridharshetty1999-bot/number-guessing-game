import random
import string

def generate_password(length):
    letters = string.ascii_lowercase
    password = ""

    for i in range(length):
        password += random.choice(letters)

    # change one letter to a number
    index = random.randint(0, length - 1)
    password = password[:index] + str(random.randint(0, 9)) + password[index+1:]

    # change one letter to uppercase
    index = random.randint(0, length - 1)
    password = password[:index] + password[index].upper() + password[index+1:]

    return password


def main():
    num = int(input("How many passwords? "))

    for i in range(num):
        length = int(input(f"Length of password #{i+1}: "))
        if length < 3:
            length = 3

        pwd = generate_password(length)
        print(f"Password #{i+1}: {pwd}")


main()
