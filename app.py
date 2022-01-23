from flask import Flask, jsonify, request, render_template, redirect, session
from flask_cors import CORS
import json

from json_check import search_word, insert_word

async_mode = None
app = Flask(__name__)
app.config.from_object(__name__)

#CORS回避
CORS(app)

#jsonファイルをASCIIでエンコードする為のもの
app.config['JSON_AS_ASCII'] = False


@app.route("/")
def index():
    json_file = open("seword.json", 'r', encoding='shift_jis')
    json_load = json.load(json_file)
    return render_template("index.html", words=json_load)


@app.route("/resive", methods=["POST"])
def resive():
    date = request.get_json()
    literal_date = date["text"]

    tmp = {"data":search_word(literal_date)}
    print(tmp)
    return tmp

@app.route("/register", methods=["POST"])
def register():
    regWord =  request.form.get("word")
    regMean = request.form.get("mean")
    tmp_dict = {"word": regWord, "mean":regMean}

    regPronounce = request.form.get("pronounce")
    if regPronounce:
        tmp_dict["pro"] = regPronounce
    
    regExample = request.form.get("example")
    if regExample:
        tmp_dict["ex"] = regExample

    regCategory = request.form.get("category")
    if regCategory:
        tmp_dict["cate"] = regCategory

    print(tmp_dict)

    insert_word(**tmp_dict)

    return render_template("index.html", message="登録が完了しました")

if __name__ == "__main__":
    app.run()