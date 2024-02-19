import json

t = open('sample-data.json')

y = json.load(t)

y = y['indata']
y = y[0]
y = y['1iPhysIf']
y = y['attributes']

for i in y:
    if i == 'mtu':
        print(y[i])
    if i == 'dn':
        print(y[i])
