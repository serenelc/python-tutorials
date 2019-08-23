pole_moves = {"butterfly": "intermediate", "ayesha": "advanced",
              "chair spin": "beginner", "allegra": "intermediate",
              "janeiro": "advanced", "superman": "intermediate"}


def list_pole_moves(dictionary):
    for key, val in dictionary.items():
        print(f"{key} is an {val} move")


def count_pole_moves(dictionary):
    vals = list(dictionary.values())
    for v in set(vals):
        num = vals.count(v)
        if num == 1:
            print(f"There is {num} {v} move")
        else:
            print(f"There are {num} {v} moves")


count_pole_moves(pole_moves)
