def filter_prime(all):
    primes = []
    for numb in all:
        if numb == 1:
            continue
        for i in range(2, int((numb/2)+1)):
            if numb%i==0:
                break
        else:
            primes.append(numb)
    print("Filtered list of prime numbers: ", primes)

all = []
n = int(input("Number of elements in list: "))
print("Write elements one by one: ")
for i in range(0,n):
    element = int(input())
    all.append(element)

filter_prime(all)