from practicals.prac_06.guitar import Guitar

# set to ask for user input or use pre-made list
USERINPUT = False


def main():
    guitars = input_type(USERINPUT)  # returns list of guitars
    if not guitars:
        return print("No guitars")
    longest_name = max(len(guitars[i].name) for i in range(0, len(guitars)))  # find longest name for dynamic formatting
    print("These are my guitars:")
    for i, guitar in enumerate(guitars):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i + 1}: {guitar.name:{longest_name}} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


def input_type(USERINPUT):
    guitars = []
    if USERINPUT:
        print("My Guitars!")
        name = input("Name: ")
        while name != "":
            year = int(input("Year: "))
            cost = float(input("Cost: "))
            print(f"{name} ({year}) : ${cost:,.2f} added.")
            guitars.append(Guitar(name, year, cost))
            name = input("Name: ")
        print("\n... snip ...\n")
    else:
        guitars.append(Guitar("Fender Stratocaster", 2014, 765.40))
        guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
        guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    return guitars


main()
