import ngrok
import time

# Create a tunnel to localhost:9000
listener = ngrok.forward(9000, authtoken_from_env=True)
print(f"Ingress established at {listener.url()}")

# Keep running
try:
    while True: time.sleep(1)
except KeyboardInterrupt:
    ngrok.disconnect()
