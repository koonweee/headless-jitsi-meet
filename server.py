from flask import Flask, request, render_template
from jitsi_client import join_call, leave_call

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start-call', methods=['POST'])
def start_call():
    call_url = request.form['call_url']
    print('Incoming request to start call to url: ' + call_url)
    join_call(call_url)
    return render_template('index.html')

@app.route('/end-call', methods=['POST'])
def end_call():
    leave_call()
    return render_template('index.html')
