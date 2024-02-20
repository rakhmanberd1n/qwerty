n=int(input())
generator=(i for i in range(n+1) if i%2==0)
for i in generator:
    print(i)