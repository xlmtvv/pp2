import json

print("Interface Status")
print("================================================================================")
print("{:<50} {:<20} {:<10} {:<5}".format("DN", "Description", "Speed", "MTU"))  
print("-------------------------------------------------- -------------------- -------  -------")

with open("data.json", "r") as obj:
    data = json.load(obj)
    for object in data['imdata']:
        dn = object['l1PhysIf']['attributes']['dn']
        descr = object['l1PhysIf']['attributes']['descr']
        speed = object['l1PhysIf']['attributes']['speed']
        mtu = object['l1PhysIf']['attributes']['mtu']

        print("{:<50} {:<20} {:<10} {}".format(dn, descr, speed, mtu))
