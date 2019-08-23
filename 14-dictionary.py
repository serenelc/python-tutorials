country_dict = {}


def countries(dictionary):
    for key, val in dictionary.items():
        print(f"{key} has the capital {val}")


while True:
    country = input("Please enter a country: ")
    capital = input("Please enter the corresponding capital: ")
    country_dict[country] = capital

    another = input("Do you want to add another? (y/n) ")
    if another != "y":
        break

countries(country_dict)
