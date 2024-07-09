# install flask in the terminal under the command pip install flask
# after installing your data will be convert to json form 
# the given data we have picked from https://stackoverflow.com/questions/52033852/python-flask-how-to-convert-a-dictionary-object-to-json
from flask import Flask   
from flask import jsonify
# from flask and conver data into jsonify

app = Flask(__name__)


@app.route('/')
def hello():
    d = {'left': 0.17037454, 'right': 0.82339555, '_unknown_': 0.0059609693}
    message = {
        'status': 200,
        'message': 'OK',
        'scores': d
    }
    resp = jsonify(message)
    resp.status_code = 200
    print(resp)
    return resp

if __name__ == '__main__':
    app.run()