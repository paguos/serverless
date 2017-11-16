import json

def handle(st):
  data = json.loads(st)
  print("ECHO: " + data['message'])
    