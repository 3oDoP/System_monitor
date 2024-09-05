import requests
from configparser import ConfigParser

def get_config():
    config = ConfigParser()
    config.read('config.ini')
    return {
        'API_TOKEN': config.get('telegram', 'API_bot'),
        'CHAT_ID': config.get('telegram', 'ID_client')
    }

def send_telegram_message(message):
    config = get_config()
    url = f"https://api.telegram.org/bot{config['API_TOKEN']}/sendMessage"
    payload = {
        'chat_id': config['CHAT_ID'],
        'text': message
    }
    try:
        response = requests.post(url, data=payload)
        response.raise_for_status()  # Проверяем на ошибки HTTP
        if not response.json().get('ok'):
            raise Exception(f"Ошибка при отправке сообщения: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при отправке сообщения: {e}")
