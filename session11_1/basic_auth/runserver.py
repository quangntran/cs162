#!/usr/bin/env python3
from flask import Flask, jsonify, render_template
from requires_authorization import requires_authorization

app = Flask(__name__)


def get_secret_message():
    return ("The secret messages are calling to me endlessly, " +
            "they call to me across the air, " +
            "the messages across the atmosphere, " +
            "they whisper in your ear, they're calling everywhere")


# This is an example JSON API endpoint which uses HTTP basic auth
@app.route('/api/secret')
@requires_authorization
def api_secret():
    return jsonify({'message': get_secret_message()})


# This is an example HTML endpoint which uses HTTP basic auth
@app.route('/')
@requires_authorization
def index():
    return render_template('index.html', message=get_secret_message())


if __name__ == '__main__':
    app.run(host='0.0.0.0')
