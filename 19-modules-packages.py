from Countries.country import Country
from Countries.calc import population_growth

thailand = Country("Thailand", "Bangkok", "Thai", "60000000")
pop = population_growth(int(thailand.population), 4)
print(f"{pop}")