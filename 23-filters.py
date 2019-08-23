grades = ['A', 'A', 'B', 'B', 'F', 'C', 'B', 'C', 'C']


def not_fail(grade):
    return grade != 'F'


print(sorted(list(filter(not_fail, grades))))

print([grade for grade in grades if grade != 'F'])