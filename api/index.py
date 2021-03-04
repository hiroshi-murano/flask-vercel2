from flask import Flask

app = Flask(__name__)


@app.route('/hello')
def index():
    return 'こんばんは'


if __name__ == '__main__':
    app.run(host='localhost', port=8080)
