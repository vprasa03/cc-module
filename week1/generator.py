import random
import json

data = {}

for i in range(9):
    data["server" + str(i)] = random.randint(1, 50)

with open("/var/www/html/data.json", "w") as outfile:
    outfile.write(json.dumps(data))
