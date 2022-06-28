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
    del i['Active Account']
    i['Day'] = idx+1
    i['Atom New Account'] = int(i['New Account'])
    i['Ava New Account'] = int(ava_data[idx]['New Account'])
    i['Dot New Account'] = int(dot_data[idx]['New Account'])
    i['Wan New Account'] = int(wan_data[idx]['New Account'])
    del i['New Account']

# Serializing json 
json_object = json.dumps(atom_data, indent = 4)
  
# Writing to sample.json
with open("new-account.json", "w") as outfile:
    outfile.write(json_object)

# Closing file
atom_f.close()
ava_f.close()
dot_f.close()
wan_f.close()
