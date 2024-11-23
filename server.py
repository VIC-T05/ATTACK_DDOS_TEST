from flask import Flask
import time

app = Flask(__name__)

@app.route('/')
def home():
    # Simulates a small delay to represent server processing
    time.sleep(0.1)
    return "Server is active"

if __name__ == '__main__':
    app.run(port=5000)  # The server will run on port 5000
