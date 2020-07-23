import json
import pytest
from pytest_mock import mocker
from random_dist import run

TESTING_URL = "https://postman-echo.com/post"
def test_send_val_post(mocker):
	expect_response = {"response": {'args': {}, 
		'data': {'val': 120},
		'files': {}, 
		'form': {}, 
		'headers': {
			'x-forwarded-proto': 'https',
			 'x-forwarded-port': '443',
			  'host': 'postman-echo.com',
				 'content-length': '12', 
				 'user-agent': 'python-requests/2.22.0', 
				 'accept-encoding': 'gzip, deflate', 
				 'accept': '*/*', 
				 'content-type': 'application/json'
				 }, 
		'json': {'val': 120},
		'url': 'https://postman-echo.com/post'
		},
		"status_code": 200
	}
	mocker.patch('random_dist.client.send_val', return_value=expect_response)
	resp = run.start(runs=1, debug=True, sleep_length=0)
	assert type(resp) is list
	assert type(resp[0]) is dict
	assert 200 == resp[0]["status_code"]
	assert '443' == resp[0]["response"]["headers"]['x-forwarded-port']