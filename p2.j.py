import random

def generate_password(pwlengths):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    passwords = []

    for length in pwlengths:
        password = ""
        for _ in range(length):
            password += random.choice(alphabet)

        password = replace_with_number(password)
        password = replace_with_uppercase_letter(password)

        passwords.append(password)

    return passwords


def replace_with_number(pword):
    for _ in range(random.randrange(1, 3)):
        replace_index = random.randrange(0, len(pword) // 2)
        pword = (
            pword[:replace_index]
            + str(random.randrange(10))
            + pword[replace_index + 1:]
        )
    return pword


def replace_with_uppercase_letter(pword):
    for _ in range(random.randrange(1, 3)):
        replace_index = random.randrange(len(pword) // 2, len(pword))
        pword = (
            pword[:replace_index]
            + pword[replace_index].upper()
            + pword[replace_index + 1:]
        )
    return pword


def main():
    num_passwords = int(input("How many passwords do you want to generate? "))
    print(f"Generating {num_passwords} passwords")
    print("Minimum length of password should be 3")

    password_lengths = []

    for i in range(num_passwords):
        length = int(input(f"Enter the length of Password #{i + 1}: "))
        if length < 3:
            length = 3
        password_lengths.append(length)

    passwords = generate_password(password_lengths)

    for i, pw in enumerate(passwords, start=1):
        print(f"Password #{i} = {pw}")


if __name__ == "__main__":
    main()



