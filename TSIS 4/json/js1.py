import json 
print("""Interface Status
================================================================================
DN                                  x.                Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------""")
with open('C:\Users\lenovo\Desktop\pp\TSIS 4\json\sample-data.json',"r")as file:
    data= json.load(file)
    for item in data['imdata']:
        print(f"{item['l1PhysIf']['attributes']['dn']}                               {item['l1PhysIf']['attributes']['speed']}  {item['l1PhysIf']['attributes']['mtu']}")