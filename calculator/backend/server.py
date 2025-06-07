'''THis server will serve all calculator queries'''

from flask import Flask, request, Response, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/ping", methods=['POST'])
def post_hello():
    '''Ping for post'''
    data = request.get_json()
    print("Data", data)
    print(data['msg'])
    # print(request.__repr__())
    
    return data

@app.route("/calc", methods=['POST'])
def calc():
    '''Calculate '''
    data = request.get_json()
    print("Data", data)
    # print(data['msg'])
    # print(request.__repr__())
    print(data['num1'], data['operator'],  data['num2'])
    
    return data

if __name__ == "__main__":
    app.run(debug=True) 