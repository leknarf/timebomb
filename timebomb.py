from flask import Flask
import socket
import time
import os

app = Flask(__name__)

@app.route('/')
def index():
    status_line = "{} - {}\n".format(
            socket.gethostname(), time.strftime("%X"))
    return status_line

@app.route('/boom', methods=['POST'])
def boom():
    os.system('killall gunicorn && rm -rf /opt/timebomb/')
    return 'boom'

if __name__ == '__main__':
    app.run()
