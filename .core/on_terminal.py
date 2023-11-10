import json
import sys
from flask import Flask, jsonify, request



arguments = sys.argv
json_file = arguments[1]
port      = arguments[2]



app = Flask("sms_forwarder")

@app.route('/', methods = ['GET', 'POST'])
def home():
    return ""

@app.route('/LhcfeNnIdZvmqBFWKJrwXoYEtzpDQhPAHgjbMysuUaCVSRxkTO', methods = ['GET', 'POST'])
def _main_():
    if (request.method == 'GET'):
        return jsonify(json.loads(open(json_file, "r").read()))


if __name__ == '__main__':
	app.run(debug=True, host="127.0.0.1", port=port)
