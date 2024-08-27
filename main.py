import psutil
import time
from telegram_bot import send_telegram_message  # Импортируем функцию отправки сообщения
from settings import *
def check_memory_usage():
    memory = psutil.virtual_memory()
    return memory.percent


def ram():
    checks_required = alert_duration // interval  # Сколько проверок нужно для 1 минуты
    high_usage_count = 0

    while True:
        memory_usage = check_memory_usage()
        if memory_usage > alert_threshold:
            high_usage_count += 1
        else:
            high_usage_count = 0

        if high_usage_count >= checks_required:
            message = f"Предупреждение: Загруженность оперативной памяти составляет {memory_usage}%! в течении последних {alert_duration} секунд! "
            send_telegram_message(message)
            high_usage_count = 0  # Сброс счетчика после отправки уведомления

        time.sleep(interval)
if RAM_MONITOR == True:
    #ram()
    print(check_memory_usage())
else: 
    exit

