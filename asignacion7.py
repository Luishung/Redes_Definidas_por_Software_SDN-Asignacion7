#Inicialmente importamos nuestro archivo asignacion7.py
import requests
import json
import time
from pprint import pprint

response = requests.post(
    'https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token',
    headers={'Authorization':'Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE='})
response.raise_for_status()
payload=response.json()
pprint(payload)
while True:
  response = requests.get(
      'https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device',
      headers={'X-Auth-Token':payload['Token']})
  List=response.json()['response']
  dicc={}
  dicc['response']=[]
  for j in range(len(List)):
    dicc['response'].append({
                  'Nombre':List[j]['family'],
                  'Estatus':List[j]['reachabilityStatus']})
  with open ('Devicesfile.json','w') as file:
    json.dump(dicc,file,indent=4)
  time.sleep(300)
  
