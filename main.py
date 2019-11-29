from flask import Flask, escape, request
import os


app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'


port = int(os.getenv('FLASK_PORT', 3000))
app.run(host='0.0.0.0', port=port)
