# Question 1
NAME_FILE = "name.txt"

name = input("Enter your name: ")
name_output = open(NAME_FILE, 'w')
print(name, file=name_output)
name_output.close()

# Question 2
name_input = open(NAME_FILE, 'r')
print("Your name is", name_input.read())
name_input.close()

# Question 3
numbers_input = open("numbers.txt", "r")
result = int(numbers_input.readline()) + int(numbers_input.readline())
print(result)
numbers_input.close()

# Question 4
result = 0
numbers_input = open("numbers.txt", 'r')
for numbers in numbers_input:
    result += int(numbers)
print(result)
numbers_input.close()

