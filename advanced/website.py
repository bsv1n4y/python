# run `python3 -m pip install flask ` to run this app
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World!!"

app.run(host='0.0.0.0', port=8080)
# After execution of command browse to http://localhost:8080 to get the web site.

