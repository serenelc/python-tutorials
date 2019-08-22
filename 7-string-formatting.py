# Way 1. The comma adds a space of its own.
name = "Serene"
surname = "Chongtrakul"
print("Name:", name, "Surname:", surname)

# Way 2. Format method (numbers correspond to the index of the vars in format(_, _, ...)
# the .3 is a precision of 3 numbers, .3f means 3 floating point numbers i.e. 3 decimal points
num1 = 1.2345667
print("Num1 3 digits: {0:.3} Num1 3 dp: {0:.3f}".format(num1))

# Way 3. Using F-Strings.
song = "Bury A Friend"
num2 = 312.3212343212
print(f"I choreographed my routine to {song}")
print(f"My number to 4 dp is: {num2:.4f}")
