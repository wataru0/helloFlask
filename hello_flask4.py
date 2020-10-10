from flask import Flask,jsonify
import json

app = Flask(__name__)
# 日本語
app.config["JSON_AS_ASCII"] = False

# jsonを返す方法
# methodで指定することで，GET,POSTでの受け取りを許可している
@app.route("/", method=["GET", "POST"]) 
def index():
    return jsonify({"language": "パイソン"}), 418

if __name__ == "__main__":
    app.run(debug=True, port=8888, threaded=True)