from flask import Flask
import socket
import time

app = Flask(__name__)

@app.route('/')
def index():
    return "{} - {}".format(
            socket.gethostname(), time.strftime("%X"))

if __name__ == '__main__':
    app.run()
