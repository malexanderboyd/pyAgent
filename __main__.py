from flask import Flask
import requests
from agent import Agent
import os
import json

app = Flask(__name__)


filename = os.path.join(app.root_path, 'agentconfig.json')
with open(filename, 'r') as f:
    config = json.load(f)
global monitorEnabled
monitorEnabled = config['agentEnabled']

if monitorEnabled:
    monitor = Agent()

@app.before_request
def add_monitor():
    if monitorEnabled:
        monitor.startRequestTimer()

@app.after_request
def check_monitor(res):
    if monitorEnabled:
        stringCount = monitor.countStrings()
        monitor.stopRequestTimer()
        print '{} {}'.format("# of string objects created:", stringCount)
        taggedResponse =  monitor.addRequestID(res)
        print '{} {}'.format("Response ID:", taggedResponse.id)
        monitor.getMemoryUsed()
        return taggedResponse.response
    else:
        return res


@app.route('/')
def hello_world():
    return requests.get('http://example.com').content


if __name__ == '__main__':
    app.run()
