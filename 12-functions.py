def greet(name='Serene', time='morning'):
    print(f"Good {time} {name}")


name = input("Enter your name: ")
time = input("Enter the time of day: ")
greet(name, time)
# If we don't pass in any params it will default to the ones we set in the function name
greet()


def area_circle(radius):
    return 3.142 * (radius ** 2)


def volume(area, height):
    return area * height

r = int(input("enter the radius: "))
volume = volume(area_circle(r), r)
print(f"The volume is {volume}")