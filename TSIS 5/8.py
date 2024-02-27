import re 
def Aa(txt):
    return re.findall(r'[A-Z][^A-Z]*',txt)
print(Aa(input()))