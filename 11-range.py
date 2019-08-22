for n in range(10):
    # 0 to 9 inclusive
    print(",,", n)

for n in range(3, 10):
    # 3 to 9 inclusive
    print("}}", n)

for n in range(2, 10, 3):
    # 2 5 8 increase in 3s from 2 to 9 inclusive
    print("qq", n)

colors = ["blue", "red", "yellow", "orange"]
for n in range(len(colors)):
    print(n, colors[n])

for n in range(len(colors) - 1, -1, -1):
    print(n, colors[n])
