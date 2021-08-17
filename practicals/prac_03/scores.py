import random

def main():
    num_scores = int(input("Enter a number of scores: "))
    for i in range(0, num_scores):
        score = gen_score()
        result = get_result(score)
        print("{} is {}.".format(score, result))

def gen_score():
    """Generates random score values"""
    return random.randint(0,100)


def get_result(score):
    """returns result for score"""
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