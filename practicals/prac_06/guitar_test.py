from practicals.prac_06.guitar import Guitar


def main():
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    print("{} get_age() - Expected 99. Got {}".format(gibson.name, gibson.get_age()))
    print("{} is_vintage - Expected True. Got {}".format(gibson.name, gibson.is_vintage()))

main()
