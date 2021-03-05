# return will terminate the function
# but yield will not terminate

def sq():
    n = 1

    while n <= 10:
        s = n * n
        yield s
        n += 1

op = sq()

for i in op:
    print(i)