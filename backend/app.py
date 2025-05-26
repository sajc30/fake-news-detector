# backend/app.py
from flask import Flask
import os # For environment variables later
# from dotenv import load_dotenv # For .env file later

# load_dotenv() # For .env file later

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from the Fake News Detector Backend! Running in VS Code on macOS."

if __name__ == '__main__':
    # port = int(os.environ.get('PORT', 5000)) # For .env file later
    app.run(debug=True, port=5000) # debug=True is for development mode