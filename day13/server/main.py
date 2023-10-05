from flask import Flask, request, render_template, make_response
import json
import uuid

app = Flask(__name__, template_folder="temps")

COOKIEID = "7715F2EE02F844EDB99E950986BA9DDA"

@app.route("/")
def index():
    # cookie验证
    login_id = request.cookies.get("login_id")
    if login_id == COOKIEID:
        return render_template("index.html")
    else:
        return "请登录"


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/auth", methods=["POST"])
def auth():
    user = request.form.get("user")
    pwd = request.form.get("pwd")
    if user == "root" and pwd == "123":
        # 写cookie
        resp = make_response("success!")
        # randomStr = uuid.uuid4().hex.upper()
        resp.set_cookie("login_id", COOKIEID)
        # COOKIEID = randomStr
        return resp
    else:
        return "fail!"


@app.route("/books")
def books():
    # cookie验证
    login_id = request.cookies.get("login_id")
    if login_id == COOKIEID:
        data = json.dumps(["西游记", "三国演义", "水浒传", "红楼梦"], ensure_ascii=False)
        return data
    else:
        return "请登录"



app.run()
