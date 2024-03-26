<<<<<<< HEAD
import os
path=input("enter the path:")
print("Only dir:\n",[name for name in os.listdir(path) if os.path.isdir(os.path.join(path,name))])
print("only files:\n",[name for name in os.listdir(path) if os.path.isfile(os.path.join(path,name))])
=======
import os
path=input("enter the path:")
print("Only dir:\n",[name for name in os.listdir(path) if os.path.isdir(os.path.join(path,name))])
print("only files:\n",[name for name in os.listdir(path) if os.path.isfile(os.path.join(path,name))])
>>>>>>> aae11a7dea5174a8b7178398d1b3773aa45b90fa
print("All things:\n",[name for name in os.listdir(path)])