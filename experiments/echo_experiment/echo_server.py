"""This module invokes repeatly an echo function with many different serverless platforms."""

import json
import requests

SNAFU_URL = 'http://localhost:10000/2015-03-31/functions/demo.lambda_handler/invocations'
FN_URL = 'http://localhost:8080/r/myapp/fn-project'
AZURE_URL = 'http://localhost:7071/api/HttpTriggerJavaScript'
KUBELESS_URL = 'http://localhost:4040/api/v1/proxy/namespaces/defaul:function-port/'
SNAFU_HEADERS = {'Content-Type': 'application/json'}
PAYLOAD = {'event':'context'}

def run(url, data, headers, count=1):
    """Run a function on a serverless runtime."""
    rem = count
    while rem > 0:
        print "Exectuion #" + str(count - rem + 1)
        req = requests.post(url, data, headers)
        print req.text
        rem = rem - 1

run(AZURE_URL, {}, {'name':'demo'}, 5)
run(SNAFU_URL, json.dumps(PAYLOAD), SNAFU_HEADERS, 5)
run(FN_URL, {}, {}, 20)


