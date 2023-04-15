import json
from datetime import datetime

ruta_archivo = "/home/devasc/labs/devnet-src/parsing/myfile.json"

with open(ruta_archivo,'r') as archivo:
    ourjson = json.load(archivo)

token = ourjson['access_token']
#fecha_caducidad = datetime.fromisoformat(ourjson['expires_in'])

#fecha_actual = datetime.now()

#tiempo_restante = fecha_caducidad - fecha_actual

print(ourjson)
print(ourjson['access_token'])    