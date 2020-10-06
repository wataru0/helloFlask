from flask import Flask

# アプリの設定
app = Flask(__name__)


@app.route('/')  # どのページで実行する関数か設定
def hello():
    name = "Hello World"
    return name

@app.route('/good')  # どのページで実行する関数か設定
def good():
    name = "Good"
    return name

@app.route('/<name>')
def hello_name(name):
    return "Hello, {}".format(name)

if __name__ == "__main__":
    # デバッグモード，localhost:8888, スレッドオン(並列処理を有効にして同時アクセスを可能にする)で実行
    app.run(debug=True, port=8888, threaded=True)