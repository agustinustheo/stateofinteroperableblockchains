import json
 
# Opening JSON file
atom_f = open('atom.json')
ava_f = open('ava.json')
dot_f = open('dot.json')
wan_f = open('wan.json')
 
# returns JSON object as
# a dictionary
atom_data = json.load(atom_f)
ava_data = json.load(ava_f)
dot_data = json.load(dot_f)
wan_data = json.load(wan_f)
 
# Iterating through the json
# list
for idx, i in enumerate(atom_data):
    del i['New Account']
    i['Day'] = idx+1
    i['Atom Active Account'] = int(i['Active Account'])
    i['Ava Active Account'] = int(ava_data[idx]['Active Account'])
    i['Dot Active Account'] = int(dot_data[idx]['Active Account'])
    i['Wan Active Account'] = int(wan_data[idx]['Active Account'])
    del i['Active Account']

# Serializing json 
json_object = json.dumps(atom_data, indent = 4)
  
# Writing to sample.json
with open("active-account.json", "w") as outfile:
    outfile.write(json_object)

# Closing file
atom_f.close()
ava_f.close()
dot_f.close()
wan_f.close()
