import os
import json
import requests

url = "http://localhost:58000/api/v1/host"

with open("artifacts/day5/pt/serviceTicket.txt", "r") as f:
    ticket = f.read().strip()

headers = {
    "X-Auth-Token": ticket,
    "Content-Type": "application/json"
}

resp = requests.get(url, headers=headers)
print(('Request status: ', resp.status_code))

if resp.status_code == 200:
    hosts = resp.json()['response']
    for host in hosts:
        print((host['hostName'], '\t', host['hostIp'], '\t', host['hostMac'], '\t', host['connectedInterfaceName']))