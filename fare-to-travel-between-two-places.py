import requests
import json

key="AIzaSyDHkUK9MjmEWAQQK5Vyc4dvMkRXbB0t3eU"  ##if there is an error while executing this program "index out of range" just change this key value by generating a new key form the site: https://console.cloud.google.com/apis/credentials?project=myproject-244611 ---> create credentials ---> API key
source="Churchgate station"
destination="Borivali station"
url="https://maps.googleapis.com/maps/api/distancematrix/json?origins="+source+"&destinations="+destination+"&key="+key

print(url)

a=requests.get(url)

print(a, a.text, type(a.text)) 

b = json.loads(a.text)
a=b['rows'][0]['elements'][0]['distance']['text']

print(a)

x=float(a.split(" km")[0])
ans_rick=x*18
ans_cab=x*40
ans_bus=x*8

print(str(ans_rick)+"Rickshaw")
print(str(ans_cab)+"Cab")
print(str(ans_bus)+"Bus")
