import psutil
import threading
import time
from telegram_bot import send_telegram_message  # Импортируем функцию отправки сообщения
from settings import *

def check_memory_usage():
    memory = psutil.virtual_memory()
    return memory.percent

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    return cpu_usage

def ram_monitor():
    checks_required = alert_duration_ram // interval_ram
    high_usage_count = 0

    while True:
        memory_usage = check_memory_usage()
        if memory_usage > alert_threshold_ram:
            high_usage_count += 1
        else:
            high_usage_count = 0

        if high_usage_count >= checks_required:
            message = (
                f"Предупреждение: Загруженность оперативной памяти составляет {memory_usage}% "
                f"в течение последних {alert_duration_ram} секунд!"
            )
            send_telegram_message(message)
            high_usage_count = 0  # Сброс счетчика после отправки уведомления

        time.sleep(interval_ram)

def cpu_monitor():
    checks_required = alert_duration_cpu // interval_cpu
    high_usage_count = 0

    while True:
        cpu_usage = check_cpu_usage()
        if cpu_usage > alert_threshold_cpu:
            high_usage_count += 1
        else:
            high_usage_count = 0

        if high_usage_count >= checks_required:
            message = (
                f"Предупреждение: Загруженность процессора составляет {cpu_usage}% "
                f"в течение последних {alert_duration_cpu} секунд!"
            )
            send_telegram_message(message)
            high_usage_count = 0 

        time.sleep(interval_cpu)
if RAM_MONITOR == True:
    threading.Thread(target=ram_monitor, daemon=True).start()
else:
    print("Мониторинг ОЗУ включен")

if CPU_MONITOR == True:
    cpu_monitor()
else:
    print("Мониторинг CPU Отключен")

