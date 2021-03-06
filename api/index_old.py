from flask import Flask, jsonify, request, make_response, render_template

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False  # jsonのレスポンスの文字化け対応


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hello', methods=['GET'])
def api01():

    contents = request.args.get('name', '')
    print('--------------------')
    print(contents)
    # username = request.json.get('name', None)
    # age = request.json.get('age', None)
    # print(username)
    # print(age)

    data = {'名前': '鈴木', '年令': 45}

    return make_response(data)


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=8080)
