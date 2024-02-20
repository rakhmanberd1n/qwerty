x=int(input())

generator_sqr=(i**2 for i in  range(x+1))
for value in generator_sqr:
    print(value)