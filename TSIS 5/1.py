import re
def ab(txt):
    if re.search('a(b*)$',txt):
        return 'Found a match!'
    else:
        return 'Not matched!' 
    

with open('row.txt', 'r', encoding='utf-8') as f:
    
    for line in f:
        x=re.findall('a(b*)$',line)

print(x)
print(ab("abb"))
print(ab("a"))
print(ab("ax"))