a = [12,35,9,5,56,24,5,34,65,5,11,345,5,44,67,5]

print(a)

for i in range(2):
    c = a.pop(0)
    a.append(c)
print(a)

replace = list(map(lambda n: n if n != 5 else "Replaced", a))
print(replace)

a.reverse()
print(a)
