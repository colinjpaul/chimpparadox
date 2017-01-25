import json

response = open(r'C:\Users\paulc1\Documents\GitWork\automation_sandbox\test_suites\wip\defect_ComponentsConfigurationFound.json', 'r')
response_content = response.read()
json_data = json.loads(response_content)

