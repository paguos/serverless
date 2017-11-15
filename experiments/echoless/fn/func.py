
import sys
import os
import json

sys.stderr.write("Starting Python Function\n")

message = "-"

try:
  if not os.isatty(sys.stdin.fileno()):
    try:
      obj = json.loads(sys.stdin.read())
      if obj["message"] != "":
        message = obj["message"]		
    except ValueError:
      # ignore it
      sys.stderr.write("no input, but that's ok\n")
except:
  pass

print "ECHO:", message,