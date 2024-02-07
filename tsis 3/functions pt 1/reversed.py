sent = input("Write a sentence: ")

new = sent.split()
new.reverse()

rev = ""
for i in new:
    rev+=i+" "

print(rev)