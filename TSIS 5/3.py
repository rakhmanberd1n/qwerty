import re
with open('row.txt', 'r', encoding='utf-8') as f:
    
    for line in f:
        x=re.findall('[а-я]+_[а-я]+$',line)
print(x)      