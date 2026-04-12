print("This is the start")
from square import Square
from square.environment import SquareEnvironment
from square.core.api_error import ApiError
from dotenv import load_dotenv
import os

load_dotenv()

client = Square(
    environment=SquareEnvironment.SANDBOX,
    token = os.environ['SQUARE_ACCESS_TOKEN'])

        

# total number of balls of yarn sold


# receive order event from Square

# check for any balls of yarn in orders


#update ticker counter

from flask import Flask, request, Response, jsonify

app = Flask(__name__)
print("Flask started")
@app.route('/', methods=['POST', 'GET']) #'/webhook' needs to be a URL that will then route here

def handle_webhook():
    if request.method == 'POST':
        try:
            payload = request.form
            print(f"Received this payload: {payload}", flush=True)
            return 'success', 201
        except Exception as e:
            print(f"Error: {e}")
            return jsonify ({"error":"Failed to process webhook"}), 401
    else:
        os.abort()
        
if __name__ == '__main__':
    print("app started")
    app.run(host='0.0.0.0', port=5000, debug=True)
