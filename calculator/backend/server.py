'''THis server will serve all calculator queries'''

from flask import Flask, request, Response, jsonify
from calc import calculate
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
    try:
        # Call your main code's function
        result = calculate(float(data['num1']), float(data['num2']), data['operator'])
        print(f"result is {result}")
        return jsonify({
            "status": "success",
            "result": result,
            "calculation": f"{data['num1']} {data['operator']} {data['num2']} = {result}"
        })
        
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 400
    return data

if __name__ == "__main__":
    app.run(debug=True) 