import requests 
import json

# api-endpoint 
URL = "http://127.0.0.1"
  
r = requests.post(url = URL, data = json.dumps({"name": "HIVENet"})) 
  
# extracting data in json format 
# data = r.json() 
  
print r
  