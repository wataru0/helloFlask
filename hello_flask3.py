from flask import Flask, render_template

# appというFlaskインスタンスを作成
app = Flask(__name__)

# このように、render_templateを使って、ファイルとしてのhtmlを出力できます。
@app.route("/", methods=["GET", "POST"])
def main_page():
    return render_template("mainpage.html")

@app.route("/<name>", methods=["GET", "POST"])
def namepage(name):
    return render_template("name.html", name=name)

if __name__ == '__main__':
    # Flaskを起動
    app.run(debug=True, port=8888, threaded=True)