# Flask API handler
A small wrapper for flask app to easy the endpoints creation

## Getting Started
This wrapper helps davide the Flask App into modules and to use __Class__ handlers instead of functions for views
## Prerequisites
The only requirement for this project is Flask  
## Usage
```python
from flask import Flask

from api_handler import ApiHandler

form example import UserHandler
form example import PaymentHandler

app = Flask(__name__)

# Init the api handler 
api = ApiHandler(app)

# Add the endpoints 
api.add_handler('/user', UserHandler)
api.add_handler('/payment', PaymentHandler)
```

## TODO
*   Make pip installable
*   Add tests