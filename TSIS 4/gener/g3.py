def is_divisble_4_3(n):
    for i in range(n+1):
        if i%3==0 and i%4==0:
            yield i 
x=int(input())
for i in is_divisble_4_3(x):
    print(i)          
            
            