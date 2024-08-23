import requests
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
API_TOKEN = config.get('telegram', 'API_bot')
CHAT_ID = config.get('telegram', 'ID_client')

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{API_TOKEN}/sendMessage"
    payload = {
        'chat_id': CHAT_ID,
        'text': message
    }
    response = requests.post(url, data=payload)
    if response.status_code != 200:
        raise Exception(f"Failed to send message: {response.text}")