"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    A ValueError occurs when the user input for either the numerator or denominator
    is a non-integer value (letters, special characters, decimals, etc...).

2. When will a ZeroDivisionError occur?
    A ZeroDivisionError occurs when the user input for the denominator is 0.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    you could ask for another input from the user that is valid (non-zero).
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("invalid input for denominator")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")