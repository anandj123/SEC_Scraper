#!/usr/bin/env python
import sys
import pprint

try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

import json

def get_jsonparsed_data(url):
    """
    Receive the content of ``url``, parse it as JSON and return the object.

    Parameters
    ----------
    url : str

    Returns
    -------
    dict
    """
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data)

#url = ("https://financialmodelingprep.com/api/financials/income-statement/FB?datatype=json")
#print(get_jsonparsed_data(url))

url = ("https://financialmodelingprep.com/api/financials/income-statement/"+sys.argv[1]+"?datatype=json")
json_dict = get_jsonparsed_data(url)
pprint.pprint(json_dict)
print(urlopen("https://financialmodelingprep.com/api/v3/company/profile/"+sys.argv[1]).read().decode("utf-8"))
print(urlopen("https://financialmodelingprep.com/api/v3/company/stock/list").read().decode("utf-8"))