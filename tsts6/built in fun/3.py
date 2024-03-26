<<<<<<< HEAD
def is_polidrom(s):
    x=list(s)
    for i in range(len(x)):
        if x[i]!=x[len(x)-i-1]:
            return "NO"
    return "Yes"
            
        
some_str=input()
=======
def is_polidrom(s):
    x=list(s)
    for i in range(len(x)):
        if x[i]!=x[len(x)-i-1]:
            return "NO"
    return "Yes"
            
        
some_str=input()
>>>>>>> aae11a7dea5174a8b7178398d1b3773aa45b90fa
print(is_polidrom(str))