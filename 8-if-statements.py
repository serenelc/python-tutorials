age = int(input("please enter your age: "))

if age < 20:
    print("You are younger than me")
elif age == 20:
    print("You are the same age as me!")
else:
    print("You are older than me")

meaty = input("Do you eat meat? (y/n) ")
if meaty == "y":
    print("You are a carnivore")
else:
    print("I'm a vegetarian too!")
    