
def main():
    email_list = {}
    email = input("Email: ")
    while email != "":
        name = get_email(email)
        confirm = input("Is your name {}? (Y/n) ".format(name))
        if confirm[0].upper() == "Y":
            pass
        else:
            name = input("Name: ")
        email_list[email] = name
        email = input("Email: ")
    [print("{} ({})".format(email_list[name], name)) for name in email_list]


def get_email(email):
    name = email.split('@')
    name = name[0].split('.')
    return " ".join(name).title()


main()
