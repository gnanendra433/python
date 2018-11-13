import json 
people_string = '''
{
	"people" :
	 [
		{
			"name": "jhon",
			"phone_num": "457238727",
			"emails" : ["ramss@gmail.com", "jdkajsdd@gmail.com"],
			"has_licence": false
		},
		{
			"name": "jinny",
			"phone_num": "898858537",
			"emails": null,
			"has_licence": true
		}

  	]
}
'''


data = json.loads(people_string)
for person in data["people"]:
	print (person)

new_string = json.dumps(data, indent = 2, sort_keys = True)
print (new_string)