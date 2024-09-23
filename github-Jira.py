# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
from flask import Flask,request,jsonify

app = Flask(__name__)

# Define a route that handles GET requests
@app.route('/createJira', methods=['POST'])
def createJira():

    url = "https://swapniljira.atlassian.net/rest/api/3/issue"

    API_TOKEN="" #replace with your token from JIRA
    auth = HTTPBasicAuth("your-email-id", API_TOKEN)

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
                            "text": "Order entry fails when selecting supplier.",
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
        "summary": "Main order flow broken",
    },
    "update": {}
    } )


    webhook = request.json
    response = None
    if webhook['comment'].get('body') == "/jira":
        response = requests.request("POST", url, data=payload, headers=headers, auth=auth)
        return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
    else:
        print('Jira issue will be created if comment includes /jira')
        return "No action taken for this comment", 200



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
