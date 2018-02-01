from flask import Flask, request
import subprocess
import re

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world'

@app.route('/control', methods=['POST'])
def home_control():
    content = request.get_json()
    if content is not None:
        device = content['device']
        operation = content['operation']
    try:
        subprocess.run('irsend SEND_ONCE {0} {1}'.format(device, operation),shell=True,check=True)
    except:
        return 'error'
    return 'success'

def device_filter(self, term):
    pass

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

