import os
import hmac
import hashlib
import base64
from dotenv import load_dotenv
from flask import Flask, request, abort, jsonify

load_dotenv()

app = Flask(__name__)

# Set these as environment variables
SQUARE_WEBHOOK_SIGNATURE_KEY = os.getenv("SQUARE_WEBHOOK_SIGNATURE_KEY")
SQUARE_WEBHOOK_NOTIFICATION_URL = os.getenv("SQUARE_WEBHOOK_NOTIFICATION_URL")


def is_valid_signature(request):
    """Verify Square webhook signature"""
    signature = request.headers.get("x-square-hmacsha256-signature")

    if not signature:
        return False

    # Create the signed payload string
    payload = SQUARE_WEBHOOK_NOTIFICATION_URL + request.data.decode("utf-8")

    # Create HMAC SHA256 hash
    computed_signature = base64.b64encode(
        hmac.new(
            SQUARE_WEBHOOK_SIGNATURE_KEY.encode("utf-8"),
            payload.encode("utf-8"),
            hashlib.sha256
        ).digest()
    ).decode("utf-8")

    # Compare signatures securely
    return hmac.compare_digest(computed_signature, signature)


@app.route("/", methods=["POST"])
def square_webhook():
    # Verify signature
    if not is_valid_signature(request):
        abort(403, description="Invalid signature")

    event = request.json
    print(event, flush=True)
    if not event:
        abort(400, description="Invalid payload")

    event_type = event.get("type")
    event_id = event.get("event_id")

    print(f"Received event: {event_type}", flush=True)
    print(f"Event ID: {event_id}", flush=True)
    print("Full payload:", event, flush=True)

    # Handle specific event types
    if event_type == "payment.created":
        payment_data = event.get("data", {}).get("object", {})
        print("Payment created:", payment_data, flush=True)

    elif event_type == "payment.updated":
        payment_data = event.get("data", {}).get("object", {})
        print("Payment updated:", payment_data, flush=True)

    # Always respond with 200 OK
    return jsonify({"status": "success"}), 200


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True, ssl_context=('/etc/letsencrypt/live/eerpi.ddns.net/fullchain.pem','/etc/letsencrypt/live/eerpi.ddns.net/privkey.pem'))
    
# figure out ssl certs for https requests 