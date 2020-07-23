from random_dist.generate import generate_json, generate_val
from unittest.mock import patch
import pytest
import datetime
import json
from random_dist import generate

def test_generate_val_tz():
    req = generate.generate_val()
    assert datetime.datetime.strptime(req["datetime"], generate.DATE_FORMAT).tzinfo

def test_generate_val_int():
    req = generate.generate_val()
    assert type(req["value"]) is int

def test_generate_json_type():
    req = generate_json()
    assert type(req) is str

def test_generate_val_ip():
    req = generate_val(ip="0.0.0.0")
    assert "ip" in req
    assert type(req["ip"]) is str
    assert "0.0.0.0" == req["ip"]