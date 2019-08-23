class Country:

    def __init__(self):
        self.name = "Thailand"
        self.capital = "Bangkok"
        self.language = "Thai"
        self.population = "60,000,000"

    def neighbours(self):
        print(f"{self.name} has neighbours Cambodia and Myanmar")

thailand = Country()
print(f"{thailand.name}'s capital is {thailand.capital}. The majority of the population"
      f"speak {thailand.language} and the population size is {thailand.population}")
thailand.neighbours()

