import random
import json

data = {}

for i in range(10):
    data["server" + str(i)] = random.randint(1, 100)

with open("/var/www/html/data.json", "w") as outfile:
    outfile.write(json.dumps(data))
