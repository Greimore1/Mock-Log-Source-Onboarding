import socket
import time
import json
import random

def generate_log():
    levels = ["INFO", "WARN", "ERROR"]
    return json.dumps({
        "host": "simulated-linux-01",
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "level": random.choice(levels),
        "message": random.choice(["User login", "File accessed", "Firewall hit", "Process started"])
    })

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    log = generate_log()
    sock.sendto(log.encode(), ("127.0.0.1", 5140))
    print(f"Sent: {log}")
    time.sleep(2)
