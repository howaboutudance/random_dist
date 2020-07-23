import time
import logging
from socket import gethostbyname, gethostname
from . import generate
from . import client

LOCAL_IP = gethostbyname(gethostname())
def start(runs=20, sleep_length=1, debug=False):
    if debug:
        rt = []
    while runs > 0:
        json_req =  generate.generate_json(ip=LOCAL_IP, iteration=runs)
        logging.debug(json_req)
        resp = client.send_val(json_req)
        logging.debug(f"sleep for {sleep_length}")
        time.sleep(sleep_length)
        if debug:
            rt.append(resp)
        runs -= 1
    if debug:
        return rt