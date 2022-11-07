import requests
import json

url = 'https://pokeapi.co/api/v2/pokemon/ditto'

response = requests.get(url).json()

#Dumps return the json object serialized
json_dumps = json.dumps(response)
print(type(json_dumps))

#Load and deserialize data to a Python object
json_loads = json.loads(json_dumps)
print(type(json_loads))

#Create json file using open() and dump() function
with open("Sample.json", "w") as p:
     json.dump(response, p)

#Read json from a file using load()
with open("Sample.json", "r") as r:
     data = json.load(r)


