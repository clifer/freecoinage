import json
import requests

def FetchAPI(address, requeststring):

    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    params = ''

    try:
        response = requests.get(address + requeststring)
        data = response.json()
        return data;
    except:
        return 'Connection failure. ' + address + requeststring
