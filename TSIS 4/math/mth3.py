from math import *
sides,lenght=int(input("Sides:")),int(input("Lenght:"))
area=(sides*pow(lenght,2))/(4*tan(pi/sides))
print("Area :",int(area))