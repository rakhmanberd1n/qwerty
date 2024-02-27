import re
def ab3(txt):
    if re.search("ab{2,3}",txt):
       return 'Found a match!'
    else:
        return 'Not matched!' 
    
with open('row.txt', 'r', encoding='utf-8') as f:
    
    for line in f:
        x=re.findall('ab{2,3}',line)
print(x)      
lista=["a",'abbb','ab','ABBB',"abbc","dfdfab","dasdasAabbb;d"]
for i in lista:
    print(ab3(i))
        