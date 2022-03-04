from ast import Num
from distutils.log import error
import requests
import sys


def print_usage(data):
    cpu_usage = {"under": 0, "over": 0}

    for key in data.keys():
        print(key + " " + str(data[key]))
        if data[key] < 50:
            cpu_usage["under"] += 1
        else:
            cpu_usage["over"] += 1

    print(cpu_usage)


if len(sys.argv) < 2:
    error("Please provide a URL as argument!")
    data = {
        "server0": 27,
        "server1": 29,
        "server2": 40,
        "server3": 31,
        "server4": 58,
        "server5": 15,
        "server6": 14,
        "server7": 3,
        "server8": 24,
        "server9": 63,
    }
    print_usage(data)
else:
    rq = requests.get(sys.argv[1])
    if rq.status_code == 200:
        data = rq.json()
        print_usage(data)
    else:
        print("Request failed with status " + str(rq.status_code))
