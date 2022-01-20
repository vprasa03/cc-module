from distutils.log import error
import requests
import sys

if len(sys.argv) < 2:
    error("Please provide a URL as argument!")
else:
    rq = requests.get(sys.argv[1])
    print("Status: " + str(rq.status_code))
    if rq.status_code == 200:
        print(rq.json())
