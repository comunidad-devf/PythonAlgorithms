import json

data = {}
data['key'] = 'value'
with open('data.json', 'w') as f:
    json.dump(data, f)
