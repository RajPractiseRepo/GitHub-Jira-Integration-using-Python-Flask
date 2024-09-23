# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://swapniljira.atlassian.net/rest/api/3/issue"

API_TOKEN = "ATATT3xFfGF0OAwWBy1NmEVvzfKUDTMUSuiUSftFbxU0VA_uN3xDbvTGLWW57a3SRAInLcHEgJCPCG6_pdTe9DKhp6UPWFh1WxNgzrP0J1IsmnNE9Z55wbfMS9YvLmX09SjLnB6Dl9Y98UxqHd7YXl7I2X4Q2y9ALiarTgQjdlW0tp-E6Z_guRc=34117EDB"

auth = HTTPBasicAuth("er.swapnil.singh93@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "fields": {
    "description": {
      "content": [
        {
          "content": [
            {
              "text": "My first jira ticket",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
    "project": {
      "key": "AB"
    },
    "issuetype": {
      "id": "10002"
    },
    "summary": "First JIRA Ticket",
  },
  "update": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))