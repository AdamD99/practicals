"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random

def main():
    score = float(input("Enter score: "))
    result = get_result(score)
    print(result)

    score = random.randint(1, 100)
    result = get_result(score)
    print (result)


def get_result(score):
    if 100 < score or score < 0:
        result = "Invalid score"
    elif score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    else:
        result = "Bad"
    return result


main()