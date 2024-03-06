FFil=open("tt.txt","r")
s=""
for i in FFil:
    s=s+i
new_file=open("New.txt","w")
new_file.write(s)