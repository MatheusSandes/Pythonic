def createSquare(until):
    list = range(until+1)
    for i in list:
        yield i**2

sqrntil10 = createSquare(10)

for i in sqrUntil10:
    print(i)
