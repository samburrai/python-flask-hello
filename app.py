from flask import Flask
import os
import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    current_time = datetime.datetime.now()
    return "Hello World " + current_time.strftime("%m/%d/%Y, %H:%M:%S")

if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port,host='0.0.0.0')