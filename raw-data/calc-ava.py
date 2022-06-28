import json
 
# Opening JSON file
f = open('ava-cumulative.json')
 
# returns JSON object as
# a dictionary
data = json.load(f)
 
# Iterating through the json
# list
for idx, i in enumerate(data):
    if idx == 14:
        i['New Account'] = 0
        break
    i['New Account'] = str(int(data[idx]['Daily Cumulative New Account']) - int(data[idx+1]['Daily Cumulative New Account']))
 
print(data)

# Closing file
f.close()