# Afinity API Server

# Server Imports
from flask import Flask, g, jsonify
from flask_cors import CORS

# Other Imports
import time
import openai

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app, supports_credentials=True)

# Apply configuration from config.py
app.config.from_pyfile('config.py')

# This happens before the request is processed
@app.before_request
def before_request():
    g.start_time = time.time()
    g.openai = openai.OpenAI(
        api_key=app.config['OPENAI_API_KEY'],
    )

# This happens after the request is processed
# This is useful for logging and other post-processing tasks
@app.after_request
def after_request(response):
    response.headers["Content-Type"] = "application/json"
    elapsed_time = time.time() - g.start_time
    print(f"LOG Time to Respond: {elapsed_time:.2f}s")
    return response

# For these requests with these methods to http://localhost:4999/ return this JSON response
@app.route(
    '/',
    methods=[
        'GET',
        'POST',
        'PUT',
        'DELETE'
    ]
)
def index():
    return jsonify({
        'status': 200,
        'message': 'Hello World!'
    })


if __name__ == '__main__':
    app.run(debug=True, port=4999)