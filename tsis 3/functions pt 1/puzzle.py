def solve(numheads, numlegs):
    rabbits = (int(numlegs)-2*int(numheads))/2 # rabbits + chickens = 35
    chickens = int(numheads) - rabbits    # 4rableg + 2 chickleg = 94
    print("The number of rabbits: ", rabbits, "The number of chickens: ", chickens)

solve(input("Number of heads: "), input("Number of legs: "))