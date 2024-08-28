from flask import Flask, render_template, jsonify
import psutil
import threading
import time

app = Flask(__name__)

# Заготовки для данных мониторинга
ram_usage_data = []
cpu_usage_data = []
gpu_usage_data = []
disk_space_data = []

def check_memory_usage():
    memory = psutil.virtual_memory()
    return memory.percent

def check_cpu_usage():
    return psutil.cpu_percent(interval=1)

def check_disk_usage():
    disk = psutil.disk_usage('/')
    return disk.percent

def ram_monitor():
    while True:
        memory_usage = check_memory_usage()
        ram_usage_data.append(memory_usage)
        if len(ram_usage_data) > 60:
            ram_usage_data.pop(0)
        time.sleep(1)

def cpu_monitor():
    while True:
        cpu_usage = check_cpu_usage()
        cpu_usage_data.append(cpu_usage)
        if len(cpu_usage_data) > 60:
            cpu_usage_data.pop(0)
        time.sleep(1)

def disk_monitor():
    while True:
        disk_usage = check_disk_usage()
        disk_space_data.append(disk_usage)
        if len(disk_space_data) > 60:
            disk_space_data.pop(0)
        time.sleep(1)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ram_data')
def ram_data():
    return jsonify(ram_usage_data)

@app.route('/cpu_data')
def cpu_data():
    return jsonify(cpu_usage_data)

@app.route('/disk_data')
def disk_data():
    return jsonify(disk_space_data)

if __name__ == '__main__':
    threading.Thread(target=ram_monitor, daemon=True).start()
    threading.Thread(target=cpu_monitor, daemon=True).start()
    threading.Thread(target=disk_monitor, daemon=True).start()
    app.run(debug=True)
