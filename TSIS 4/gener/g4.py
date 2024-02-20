def sqrs(a,b):
    for x in range(a,b+1):
        yield x**2
a=3
b=8
for i in sqrs(a,b):
    print(i)