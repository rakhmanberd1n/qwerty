import os
if os.path.exists("New.txt"):
    os.remove("New.txt")
else:
    print("File daesnt exist")