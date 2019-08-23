file = open("Files/pole-moves.txt")

for line in file:
    print(line.rstrip())


file.seek(10)
lines = file.read(25)
print(lines)

file.close()

with open("Files/pole-moves.txt") as pole_file:
    def filter_moves(line):
        return '>' not in line

    lines = pole_file.readlines()

    print([line.capitalize() for line in filter(filter_moves, lines)])