from flask import Flask
from flask import request
from flask import json
from gitQueue import addData

import redis
from rq import Queue

q = Queue(connection=redis.Redis())

app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello 🙂'


@app.route('/githubdata', methods=['POST'])
def apiMessage():

    if request.headers['Content-Type'] == 'application/json':
        job = q.enqueue(addData, json.dumps(request.json))

        return json.dumps(request.json)

    return "error"


if __name__ == '__main__':
    app.run(debug=True)


