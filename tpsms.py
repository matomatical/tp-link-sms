import requests

ADDR = '192.168.1.1'
USER = 'admin'
PASS = 'admin'
AUTH = 'Basic YWRtaW46MjEyMzJmMjk3YTU3YTVhNzQzODk0YTBlNGE4MDFmYzM='
# AUTH is just base64 encoded user + pass + / + ip (I think?)

COOKIES = {'Authorization': AUTH}

def login():
    # send the login info to get the random key
    login_url = f'http://{ADDR}/userRpm/LoginRpm.htm?Save=Save'
    index_redirect = requests.get(login_url, cookies=COOKIES)

    # extract the key from the response
    key = index_redirect.text[86:102] # fragile :3
    return key

def send(key, to, msg): 
    send_url = f'http://{ADDR}/{key}/userRpm/lteWebCfg'
    message_json = {
        'module': 'message',
        'action': 3, # send SMS
        'sendMessage': {
            'to': to,
            'textContent': msg,
            # do we need the send time?
        }
    }
    headers = {
        'Origin': f'http://{ADDR}',
        'Referer': f'http://{ADDR}/{key}/userRpm/_lte_SmsNewMessageCfgRpm.htm'
    }
    response = requests.post(send_url, cookies=COOKIES,
                    json=message_json, headers=headers)
    return response.ok and response.json()['result'] == 0

key = login()
send(key, input('Phone number: '), 'hello!')
