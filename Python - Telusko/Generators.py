#return will terminate the function. but yield will not terminate.
def TopTen():

    n = 1
    while n <= 10:
        sq = n * n
        yield sq
        n += 1

values = TopTen()

#print(values.__next__())
for i in values:
    print(i)
