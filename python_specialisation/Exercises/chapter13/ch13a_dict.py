import json
data = '''{
    "name": "Chuck",
    "phone": {
        "type" : "intl",
        "number" : "+1 734 303 4456"
    },
    "email" : {
        "hide" : "yes"
    }
}'''

#deserialise from string to internal structure
#this returns a dictionary
info = json.loads(data)

print 'Name: ', info["name"]
print 'Hide: ', info["email"]["hide"]
