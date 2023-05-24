from flask import Flask, request
from jitsi_client import join_call, leave_call

app = Flask(__name__)

@app.route('/')
def hello_world():
    print('is this a console only statement?')
    return 'Hello, World!'

@app.route('/start-call', methods=['POST'])
def start_call():
    call_url = request.form['call_url']
    print('Incoming request to start call to url: ' + call_url)
    join_call(call_url)
    return 'success'

@app.route('/end-call', methods=['POST'])
def end_call():
    leave_call()
    return 'success'
