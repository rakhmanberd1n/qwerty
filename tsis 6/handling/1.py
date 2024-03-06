import os
path=input("enter the path:")
print("Only dir:\n",[name for name in os.listdir(path) if os.path.isdir(os.path.join(path,name))])
print("only files:\n",[name for name in os.listdir(path) if os.path.isfile(os.path.join(path,name))])
print("All things:\n",[name for name in os.listdir(path)])