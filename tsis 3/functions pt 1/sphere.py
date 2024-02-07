import math
def sphere_vol(radius):
    return (4/3)*math.pi*math.pow(radius,3)

print("Volume of a sphere is: ", sphere_vol(int(input("Give me radius: "))))