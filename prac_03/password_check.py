
def main():
    password = get_password()
    print_password(password)


def get_password():
    MIN_LEN = 5
    password = input("Enter Password: ")
    while len(password) < MIN_LEN:
        password = input("Enter Password: ")
    return password


def print_password(password):
    print("*" * len(password))


main()