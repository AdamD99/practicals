class Guitar:

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost
        self.age = 2021 - self.year

    def __str__(self):
        return "{} ({}) : ${:,.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        return 2021 - int(self.year)
        # return "The {} is {} years old.".format(self.name, self.age)

    def is_vintage(self):
        return self.get_age() >= 50
