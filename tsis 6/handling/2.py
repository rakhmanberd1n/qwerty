import os
path=input("enter th path:")
print("existence",os.access(path,os.F_OK))
print("readability",os.access(path,os.R_OK))
print("writability",os.access(path,os.W_OK))
print("executability",os.access(path,os.X_OK))