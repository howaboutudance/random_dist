from random import randint
import json
import datetime
from dateutil.tz import tzlocal
DATE_FORMAT = "%d %b %Y %H:%M %z"

def generate_val(limit=300, **kwargs):
  return {"value": randint(0, limit), 
		"datetime": datetime.datetime.now(tzlocal()).strftime(DATE_FORMAT),
		**kwargs
		}

def generate_json(limit=300, **kwargs):
	return json.dumps(generate_val(limit, **kwargs))