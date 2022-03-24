import json
import demjson

var = {
	"Subjects": {
				"Maths":85,
				"Physics":90
				}
	}
with open("Sample.json", "w") as p:
	json.dump(var, p)

with open("Sample.json", "r") as read_it:
	data = json.load(read_it)
print(data)

json_var ="""
{
	"Country": {
		"name": "INDIA",
		"Languages_spoken": [
			{
				"names": ["Hindi", "English", "Bengali", "Telugu"]
			}
		]
	}
}
"""
var = json.loads(json_var)
print(var)

# storing marks of 3 subjects
var = [{"Math": 50, "physics":60, "Chemistry":70}]
print(demjson.encode(var))

print(var)
