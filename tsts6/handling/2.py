<<<<<<< HEAD
import os
path=input("enter th path:")
print("existence",os.access(path,os.F_OK))
print("readability",os.access(path,os.R_OK))
print("writability",os.access(path,os.W_OK))
=======
import os
path=input("enter th path:")
print("existence",os.access(path,os.F_OK))
print("readability",os.access(path,os.R_OK))
print("writability",os.access(path,os.W_OK))
>>>>>>> aae11a7dea5174a8b7178398d1b3773aa45b90fa
print("executability",os.access(path,os.X_OK))