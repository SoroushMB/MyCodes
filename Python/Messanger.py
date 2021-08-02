import requests
import json
url = "https://www.fast2sms.com/dev/bulk"
my_data = {
    'Soroush': 'FSTSMS',
    'message': 'This is a test',
    'language': 'english',
    'route': 'p',
    'numbers': '+989114331849'
}
headers = {
    'authorization': '386732',
    'Content-Type': "application/x-www-form-urlencoded",
    'Cache-Control': "no-cache"
}
response = requests.request("POST",
                            url,
                            data = my_data,
                            headers = headers)
returned_msg = json.loads(response.text)
print(returned_msg['message'])