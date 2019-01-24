""" Sample App """

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    """ Route for home page. """

    return 'Flask Dockerized'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
