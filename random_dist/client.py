import requests
import os

if not "CLIENT_URL" in os.environ:
  DEFAULT_URL = "localhost:8080"
else:
  DEFAULT_URL = os.environ["CLIENT_URL"]

def send_val(doc, url=DEFAULT_URL):
  resp = requests.post(url, json=doc)
  return {"response": resp, "status_code": 200}