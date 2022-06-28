import json
 
# Opening JSON file
ava_f = open('raw-data/ava.json')
 
# returns JSON object as
# a dictionary
data = json.load(ava_f)
 
# Iterating through the json
# list
for idx, i in enumerate(data):
    del i['Date']
    i['Day'] = idx+1
    i['Active Account'] = int(i['Active Account'])
    i['New Account'] = int(i['New Account'])

# Serializing json 
json_object = json.dumps(data, indent = 4)
  
# Writing to sample.json
with open("ava.json", "w") as outfile:
    outfile.write(json_object)

# Closing file
ava_f.close()
 
# Opening JSON file
dot_f = open('raw-data/dot.json')
 
# returns JSON object as
# a dictionary
data = json.load(dot_f)
 
# Iterating through the json
# list
for idx, i in enumerate(data):
    del i['Date']
    i['Day'] = idx+1
    i['Active Account'] = int(i['Active Account'])
    i['New Account'] = int(i['New Account'])

# Serializing json 
json_object = json.dumps(data, indent = 4)
  
# Writing to sample.json
with open("dot.json", "w") as outfile:
    outfile.write(json_object)

# Closing file
dot_f.close()
 
# Opening JSON file
wan_f = open('raw-data/wan.json')
 
# returns JSON object as
# a dictionary
data = json.load(wan_f)
 
# Iterating through the json
# list
for idx, i in enumerate(data):
    del i['Date']
    i['Day'] = idx+1
    i['Active Account'] = int(i['Active Account'])
    i['New Account'] = int(i['New Account'])

# Serializing json 
json_object = json.dumps(data, indent = 4)
  
# Writing to sample.json
with open("wan.json", "w") as outfile:
    outfile.write(json_object)

# Closing file
wan_f.close()
 
# Opening JSON file
atom_f = open('raw-data/atom.json')
 
# returns JSON object as
# a dictionary
data = json.load(atom_f)
 
# Iterating through the json
# list
for idx, i in enumerate(data):
    del i['Date']
    i['Day'] = idx+1
    i['Active Account'] = int(i['Active Account'])
    i['New Account'] = int(i['New Account'])

# Serializing json 
json_object = json.dumps(data, indent = 4)
  
# Writing to sample.json
with open("atom.json", "w") as outfile:
    outfile.write(json_object)

# Closing file
atom_f.close()
