"""This module invokes repeatly an echo function with many different serverless platforms."""

import sys
import getopt
import requests

AZURE_URL = 'http://localhost:7071/api/echoless'
FN_URL = 'http://localhost:8080/r/echoless/echo'
KUBELESS_URL = 'http://192.168.99.100:31864/proxy'
OPENFAAS_URL = 'http://localhost:8080/function/echoless'
SNAFU_URL = 'http://localhost:10000/2015-03-31/functions/echo.lambda_handler/invocations'

JSON_HEADER = {'Content-Type': 'application/json'}

def run(url, data, headers, count=1):
    """Run a function on a serverless runtime."""
    rem = count
    while rem > 0:
        print "Exectuion #" + str(count - rem + 1)
        req = requests.post(url, data, headers)
        print req.text
        rem = rem - 1

def main(argv):
    """Run a function on a serverless runtime."""
    runtime = ''
    text = ''
    count_str = ''

    try:
        opts, args = getopt.getopt(argv,"hr:m:c:t",["runtime=","message=","count=","threads="])
    except getopt.GetoptError:
        print 'USAGE: test.py -r <runtime> -m <message> -c <count>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'USAGE: test.py -r <runtime> -m <message> -c <count>'
            sys.exit()
        elif opt in ("-r", "--runtime"):
            runtime = arg
        elif opt in ("-m", "--message"):
            text = arg
        elif opt in ("-c", "--count"):
            count_str = arg
    try:
        execute(runtime, text, int(count_str))
    except ValueError:
        execute(runtime, text)

def execute(runtime, text, count=1):
    """Run a function on a serverless runtime."""

    payload = '''{"message": "%s" }''' % text

    if runtime == 'azure':
        run(AZURE_URL, payload, JSON_HEADER, count)
    elif runtime == 'fn':
        run(FN_URL, payload, JSON_HEADER, count)
    elif runtime == 'kubeless':
        kubeless_payload = {'url':"http://localhost:8080/api/v1/proxy/namespaces/default/services/post-python:8080", 'method': "post"}
        kubeless_payload['json'] = payload
        run(KUBELESS_URL, kubeless_payload, JSON_HEADER, count)
    elif  runtime == 'openfaas':
        run(OPENFAAS_URL, payload, JSON_HEADER, count)
    elif  runtime == 'snafu':
        run(SNAFU_URL, payload, JSON_HEADER, count)
    else:
        print "Please choose one of the following runtimes:\n azure\n fn\n kubeless\n snafu"
        sys.exit()

if __name__ == "__main__":
    main(sys.argv[1:])
