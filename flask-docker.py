from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'now learning jenkns'


@app.route('/home')
def home():
    return 'this is home route'


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
