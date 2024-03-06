def is_polidrom(s):
    x=list(s)
    for i in range(len(x)):
        if x[i]!=x[len(x)-i-1]:
            return "NO"
    return "Yes"
            
        
some_str=input()
print(is_polidrom(str))