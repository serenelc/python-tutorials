flower = "lily"

def print_flower():
    global flower # overrides the global variable
    flower = "hibiscus"
    print(f"Inside the function the flower is {flower}")


print_flower()
print(f"Outside the function the flower is {flower}")