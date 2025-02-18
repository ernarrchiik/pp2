import json
file_path = "sample_data.json"
with open(file_path,'r') as file:
    data = json.load(file)
print("interface Status")
print("="*80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<10}{'MTU'}")
print("-"*50,"-"*20,"-"*9,"-"*8)
for item in data["imdata"]:
    dn = item["l1PhysIf"]["attributes"]["dn"]
    speed = item["l1PhysIf"]["attributes"]["speed"]
    mtu = item["l1PhysIf"]["attributes"]["mtu"]
    print(f"{dn:<50} {'':<20} {speed:<10} {mtu:<6}")