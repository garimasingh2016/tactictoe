'''
#!flask/bin/python

from flask import Flask, jsonify, abort, request, make_response, url_for
from flask_cors import CORS, cross_origin
import requests

app = Flask(__name__)
cors = CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'

@app.rout('/models', methods=['POST'])
@cross_origin()
def model():
    data = request.files['model_name']
    return(jsonify({'thing':'this is a thing'}))


if __name__='main':
    app.run(debug='True')
'''