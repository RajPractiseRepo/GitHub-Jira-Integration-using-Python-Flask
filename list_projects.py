import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://swapniljira.atlassian.net/rest/api/3/project"

API_TOKEN = ""

auth = HTTPBasicAuth("your-mail-id", API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

output= json.loads(response.text)

for value in output:
    print(value["name"])