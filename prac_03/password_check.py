MIN_LEN = 5

password = input("Enter Password: ")

while len(password) < MIN_LEN:
    password = input("Enter Password: ")

print("*"*len(password))