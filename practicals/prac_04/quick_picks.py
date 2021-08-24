import random

number_quickpicks = int(input("How many quick picks? "))

NUMBERSPERLINE = 6
RANGELOWER = 1
RANGEUPPER = 45

def main():
    for i in range(0, number_quickpicks):
        quickpicks = []
        for ii in range(0, NUMBERSPERLINE):
            number = random.randint(RANGELOWER, RANGEUPPER)
            while number in quickpicks:
                number = random.randint(RANGELOWER, RANGEUPPER)
            quickpicks.append(number)
            quickpicks.sort()
        quickpicks_print = ""
        for number in quickpicks:
            quickpicks_print += " {:2}".format(number)
        print(quickpicks_print)

main()

