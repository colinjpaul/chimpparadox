import json
input = '''[
    {   "id" : "001",
        "x" : "2",
        "name" : "chuck"
    },
    {   "id" : "009",
        "x" : "7",
        "name" : "Chuck"
    }
]'''

info = json.loads(input)

print 'User count: ', len(info)
