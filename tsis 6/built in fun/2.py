Some_str=input()
Upper_letter=0
lower_letter=0
for i in Some_str:
    if i.isupper():
        Upper_letter+=1
    else:
        lower_letter+=1
print(f"The number of Upper case letter is:{Upper_letter}\nThe number of lower case letter is:{lower_letter}")
        