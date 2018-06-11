# Flask API handler
A small wrapper for a Flask app to simplify endpoints creation

## Motivation
At my company, we've been using Flask-RESTful for a lot of projects for the past couple of years, and when we mapped exactly what we need from it, it was mostly the way it allows the user to add routing.

This small module replace for us this functionality, so I've decided to share it with whoever want to give it a try :wink: 

## Getting Started
This wrapper helps davide the Flask App into modules and to use __Classes__ instead of functions for views.

Just run pip install and you are good to go: 
```bash
$ pip install flask-api-handler
```

## Prerequisites
The only requirement for this project is Flask.
  
## Usage
```python
from flask import Flask
from flask import jsonify
from flask_api_handler import ApiHandler

form example import PaymentHandler

app = Flask(__name__)

# Init the api handler 
api = ApiHandler(app)

class UserHandler(object):
    def get(self):
        return jsonify({"user": "user object example"})
    def put(self):
        return jsonify({"user": "update user example"})

# Add the endpoints 
api.add_handler('/user', UserHandler)
api.add_handler('/payment', PaymentHandler)
```

## TODO
*   ~~Make pip installable~~ - DONE
*   Add tests
