class Country:

    planet = "Earth"

    def __init__(self, name, capital, language, population):
        self.name = name
        self.capital = capital
        self.language = language
        self.population = population

    def neighbours(self):
        print(f"{self.name} has neighbours Cambodia and Myanmar")

    @classmethod
    def commons(cls):
        return f"All countries are on {cls.planet}"

    @staticmethod
    def continent(continent):
        return f"{continent} is one of the continents of the world"


thailand = Country("Thailand", "Bangkok", "Thai", "60,000,000")
print(f"{thailand.name}'s capital is {thailand.capital}. The majority of the population"
      f" speak {thailand.language} and the population size is {thailand.population}")
thailand.neighbours()
print(Country.commons()) # These 2 are the same
print(thailand.commons())
print(thailand.continent("Asia"))