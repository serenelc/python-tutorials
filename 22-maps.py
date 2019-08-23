from random import shuffle


desserts = ['brownies', 'cookies', 'sticky toffee pudding', 'fudge']
def jumble(word):
    anagram = list(word)
    shuffle(anagram)
    return '-'.join(anagram)


print(jumble("serene"))
[print(x) for x in map(jumble, desserts)]
print([jumble(word) for word in desserts])
