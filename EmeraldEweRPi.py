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
    
try:
    response = client.locations.list()
    for location in response.locations:
        print(f"{location.id}: ", end ="")
        print(f"{location.name}: ", end ="")
        print(f"{location.address}: ", end ="")
except ApiError as e:
    for error in e.errors:
        print(error.category)
        print(error.code)
        print(error.detail)
        

# total number of balls of yarn sold


# receive order event from Square

# check for any balls of yarn in orders


#update ticker counter

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST']) #'/webhook' needs to be a URL that will then route here




def handle_webhook():
    if request.method == 'POST':
        try:
            payload = request.json
            print(f"Received this payload: {payload}")
            return jsonify({"message": "Webhook received successfully"}), 205
        except Exception as e:
            print(f"Error: {e}")
            return jsonify ({"error":"Failed to process webhook"}), 401
    else:
        return jsonify({"message": "method now allowed"}), 406
        
if __name__ == '__main__':
    app.run(debug=True)