from flask import Flask

# create a new Flask instance called app
app = Flask(__name__)

# Create the root (starting point) 
@app.route('/')
def hello_world():
    return 'Hello world'