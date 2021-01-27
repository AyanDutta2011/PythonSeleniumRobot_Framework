from functools import reduce

nums = [2,4,5,6,10,13,15,18,20]

evens = list(filter(lambda a: a % 2 == 0,nums))
print("Evens numbers are : ", evens)

doubles = list(map(lambda z: z * z ,evens))
print("Doubles numbers are : ", doubles)

sum = reduce(lambda a,b: a + b,doubles)
print("Sum of doubles numbers are : ",sum)


