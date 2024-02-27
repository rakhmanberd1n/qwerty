import re

# Initialize z and v outside the loop
z = []
v = []

# Open the file
with open('row.txt', 'r', encoding='utf-8') as f:
    # Iterate over each line in the file
    for line in f:
        # Find sequences of one uppercase Cyrillic letter followed by lowercase Cyrillic letters
        x = re.findall(r'\b[А-Я][а-я]+\b', line)
        # Find sequences of one uppercase Latin letter followed by lowercase Latin letters
        y = re.findall(r'\b[A-Z][a-z]+\b', line)
        
        # Append x to z if not empty
        if x:
            z.extend(x)
        # Append y to v if not empty
        if y:
            v.extend(y)

# Print the results outside the loop
print("Cyrillic:", z)
print("Latin:", v)