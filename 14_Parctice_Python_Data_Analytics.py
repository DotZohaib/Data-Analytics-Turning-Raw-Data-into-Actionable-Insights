# dic convert to the json file 

import json 

data = {'name': 'zohaib', 'age': 20, 'city': 'New York'}
print(type(data))
f = open('data.json', 'w')
json_data = json.dumps(data, indent=4, sort_keys=True) # indent is used for the space in json file
f.write(json_data)
print(json_data)
print(type(json_data))