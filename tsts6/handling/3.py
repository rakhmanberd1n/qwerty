<<<<<<< HEAD
import os
path=input("Enter the path:")
if os.access(path,os.F_OK):
    print(os.path.basename(path))
else:
=======
import os
path=input("Enter the path:")
if os.access(path,os.F_OK):
    print(os.path.basename(path))
else:
>>>>>>> aae11a7dea5174a8b7178398d1b3773aa45b90fa
    print("This path doesnt exist!")