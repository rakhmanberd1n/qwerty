import os
path=input("Enter the path:")
if os.access(path,os.F_OK):
    print(os.path.basename(path))
else:
    print("This path doesnt exist!")