from flask import Flask,request
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return  "hello world"

@app.route('/post',methods=['POST'])
def post_data():
    data = request.get_json(force=True)
    print(data)
    return json.dumps(data)
    