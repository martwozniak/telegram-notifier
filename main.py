import requests
import json

import sys

import datetime

import os
from dotenv import load_dotenv
load_dotenv()


# Main function of notifier
def send_telegram_message(message: str,
                          chat_id: str,
                          api_key: str,
                          proxy_username: str = None,
                          proxy_password: str = None,
		  proxy_url: str = None):
    responses = {}

    proxies = None
    if proxy_url is not None:
        proxies = {
            'https': f'http://{username}:{password}@{proxy_url}',
            'http': f'http://{username}:{password}@{proxy_url}'
        }
    headers = {'Content-Type': 'application/json',
                'Proxy-Authorization': 'Basic base64'}
    data_dict = {'chat_id': chat_id,
                    'text': message,
                    'parse_mode': 'HTML',
                    'disable_notification': True}
    data = json.dumps(data_dict)
    url = f'https://api.telegram.org/bot{api_key}/sendMessage'
    response = requests.post(url,
                                data=data,
                                headers=headers,
                                proxies=proxies,
                                verify=False)
    print(response) # 4 Debugging not important
    return response


# Get Secret Keys from .env file 
# Remember to create .env base on .env.example
chat_id = os.getenv('chat_id')
api_key = os.getenv('api_key')


# Call method if error occurs, then notification is pushed to telegram
n = len(sys.argv)
now = str(datetime.datetime.now())
if n<2:
    temp_message = "🔥 Site is down! You have to check it now. ⏰" + " " + now;
    send_telegram_message(temp_message, chat_id, api_key)
else:
    temp_message = sys.argv[1] + " ⏰ " + now;
    send_telegram_message(temp_message, chat_id, api_key)
