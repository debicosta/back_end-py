from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/get_sum', methods=['GET']) 
def get_sum(x,y):
    result = x+y
    return jsonify(result)
