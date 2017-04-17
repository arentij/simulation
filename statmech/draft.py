import random
import json
from pprint import pprint

N = 10
state = [random.choice([1, -1]) for i in range(N)]

a = {}
a[N] = {'J': 1}
a[N]['state'] = state

print(a)

with open('test.json', 'w') as fp:
    json.dump(a, fp)


with open('test.json') as json_data:
    d = json.loads(json_data)
    json_data.close()
    pprint(d)


