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
