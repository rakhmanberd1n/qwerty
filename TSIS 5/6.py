import re 
def replace_space(txt):
    return re.sub("\s",":",txt)
print(replace_space(input()))