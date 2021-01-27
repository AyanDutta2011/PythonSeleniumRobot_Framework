from functools import reduce

nums = [23,56,199,204,478,7634,347848]

even = list(filter(lambda n: n%2 == 0,nums))
print(even)

double = list(map(lambda n: n*n,nums))
print(double)

sum = reduce(lambda a,b: a + b,nums)
print(sum)


