def isprime(numb):
    if numb == 1:
        return False
    for i in range(2, int((numb/2)+1)):
        if numb%i==0:
            return False
    return True

all = []
n = int(input("Number of elements in list: "))
print("Write elements one by one: ")
for i in range(0,n):
    element = int(input())
    all.append(element)

primes = list(filter(lambda a:isprime(a), all))

print("Filtered list of prime numbers: ", primes)
print("And original list: ", all)