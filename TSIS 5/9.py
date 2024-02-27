import re
def insert_space(txt):
    x=re.findall("[A-Z]?[a-z]*",txt)
    y=""
    for i in x:
        if y!="":
            y=y+" "+i
        else:
            y+=i
            
    return y
print(insert_space(input()))
        