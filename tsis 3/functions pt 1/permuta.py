import itertools

Net = input("Write a string: ")

perms = itertools.permutations(Net)

for t in perms:
    print(t)