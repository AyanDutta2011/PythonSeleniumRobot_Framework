from functools import reduce

nums = [1,2,3,4,5,6,7,8,9,10]

even = list(filter(lambda n: n%2 == 0,nums))
print(even)

double = list(map(lambda n: n*n,nums))
print(double)

sum = reduce(lambda a,b: a + b,nums)
print(sum)

#replace
rep = list(map(lambda n: n if n!= 5 else "Replaced", nums))
print(rep)
