#!/usr/bin/python3

import json

from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)


def _headers_as_string(headers):
    results = ''
    for key, value in headers:
        if value:
            results += '{}: {}\n'.format(key, value)
    return results


def _headers_as_object(headers):
    results = {}
    for key, value in headers:
        results[key] = value
    return json.dumps(results)


@app.route('/')
def api_root():
    return 'IP Mirror Server'


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp


@app.route("/ip", methods=["GET"])
def api_ip():
    if 'format' in request.args and request.args['format'].upper() == 'JSON':
        return jsonify({'ip': request.remote_addr}), 200
    else:
        return request.remote_addr, 200


@app.route("/headers", methods=["GET"])
def api_headers():
    if 'format' in request.args and request.args['format'].upper() == 'JSON':
        results = {}
        for key, value in request.headers:
            results[key] = value
        return jsonify(results), 200
    else:
        results = ''
        for key, value in request.headers:
            results += '{}: {}\n'.format(key, value)
        return results, 200


if __name__ == '__main__':
    app.run(host='0.0.0.0')

