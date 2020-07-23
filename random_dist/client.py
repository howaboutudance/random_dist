import requests

DEFAULT_URL = "localhost:8080"

def send_val(doc, url=DEFAULT_URL):
    resp = requests.post(url, json=doc)
    return {"response": resp, "status_code": 200}