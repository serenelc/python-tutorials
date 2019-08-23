prizes = [5, 10, 50, 100, 500, 1000]

#list comprehension to double everything instead of for loop
prizes_doubled = [p * 2 for p in prizes]
print(prizes_doubled)

nums = [1,2,3,4,5,6,7,8,9,10]
evens_squared = [n ** 2 for n in nums if n % 2 == 0]
print(evens_squared)