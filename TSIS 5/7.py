import re
def camel_case(txt):
    x=re.split("_",txt)
    y=""
    for i in x:
        if x[0]!=i:
         i=i[0].upper()+i[1:]
        y+=i
    return y
print(camel_case(input()))