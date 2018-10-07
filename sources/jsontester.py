import requests
import datetime
import json

testData = [['0103015366f82129771b1aff4c0002155dd7902261f045538b677bec4d79cc0400320064bfb9', datetime.datetime(2018, 10, 7, 9, 6, 53, 581593)],
['010300e564ea034b241c1bff75004204018000244b03ea64e5264b03d5733a01c00000000000a0', datetime.datetime(2018, 10, 7, 9, 6, 53, 766889)],
['010300e564ea034b241c1bff75004204018000244b03ea64e5264b03d5733a01c000000000009f', datetime.datetime(2018, 10, 7, 9, 6, 53, 922366)],
['010300e564ea034b241c1bff75004204018000244b03ea64e5264b03d5733a01c00000000000a0', datetime.datetime(2018, 10, 7, 9, 6, 54, 71683)],
['0103015366f82129771b1aff4c0002155dd7902261f045538b677bec4d79cc0400320064bfb5', datetime.datetime(2018, 10, 7, 9, 6, 54, 95368)],
['010300e564ea034b241c1bff75004204018000244b03ea64e5264b03d5733a01c00000000000a0', datetime.datetime(2018, 10, 7, 9, 6, 54, 222215)]]

content = {
        'id': 'aslan',
        'name': 'faez',
        'mac' : '12:25:36',
        'ts' : str(datetime.datetime.utcnow()),
        'data' : str(testData)
    }
print (json.dumps(content))
print(requests.post('http://hook.ubeac.io/B9CRRQmc', json=json.dumps(content)))


url = "http://hook.ubeac.io/B9CRRQmc"
querystring = {"foo":["bar","baz"]}
payload = "{\"foo\": \"bar\"}"
headers = {
    'cookie': "foo=bar; bar=baz",
    'accept': "application/json",
    'content-type': "application/json",
    'x-pretty-print': "2"
    }
response = requests.request("POST", url, data=payload, headers=headers, params=querystring)