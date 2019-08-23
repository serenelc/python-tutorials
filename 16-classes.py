class Country:

    def __init__(self, name, capital, language, population):
        self.name = name
        self.capital = capital
        self.language = language
        self.population = population

    def neighbours(self):
        print(f"{self.name} has neighbours Cambodia and Myanmar")


thailand = Country("Thailand", "Bangkok", "Thai", "60,000,000")
print(f"{thailand.name}'s capital is {thailand.capital}. The majority of the population"
      f" speak {thailand.language} and the population size is {thailand.population}")
thailand.neighbours()
