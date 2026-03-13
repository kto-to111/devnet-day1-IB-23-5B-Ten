import os
import json
import requests

url = "http://localhost:58000/api/v1/network-device"
with open("artifacts/day5/pt/serviceTicket.txt", "r") as f:
    ticket = f.read().strip()

headers = {
    "X-Auth-Token": ticket,
    "Content-Type": "application/json"
}

resp = requests.get(url, headers=headers)
print(('Request status: ', resp.status_code))

if resp.status_code == 200:
    devices = resp.json()['response']
    for dev in devices:
        print((dev['hostname'], '\t', dev['platformId'], '\t', dev['managementIpAddress']))