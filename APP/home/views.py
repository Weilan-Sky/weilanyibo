# coding:utf8
from . import home
from APP import db,app
from flask import render_template, redirect, url_for, json, request
from APP.models import User
import os

@home.route("/")
def index():
    return render_template("home/home.html")


@home.route("/login/")
def login():
    return "登录"


@home.route("/logout/")
def logout():
    return "退出"


@home.route("/regist/", methods=['POST'])  # post
def regist():  # 在添加用户名前，查找数据库是否存在用户
    json_data = {}
    data={}
    if request.method == 'POST':
        print(data)
        data = request.get_data()
        print(data)
        json_data = json.loads(data)
        print(json_data)

    tag = User.query.filter_by(name=json_data["name"]).count()
    # tag = User.query.filter_by(name="weilan3").count()

    if tag == 1:
        json_data['SUCCESS'] = 'faile'
        return json.dumps(json_data, ensure_ascii=False)
    user = User(
        name=json_data['name'],
        password=json_data['password']

    )
    db.session.add(user)
    db.session.commit()
    json_data['SUCCESS'] = 'SUCCESS'
    return json.dumps(json_data, ensure_ascii=False)


@home.route("/regist/logout/")
def registlogout():
    return "注销"


@home.route("/getjson/")
def getjson():
    s = ['张三', '年龄', '姓名']
    t = {}
    for num in range(1, 5):
        t[str(num)] = s
    data = {}
    data['SUCCESS'] = 'SUCCESS'
    data['data'] = t
    return json.dumps(data, ensure_ascii=False)


@home.route("/getpostjson/", methods=["POST"])
def getpostjson():
    if request.method == 'POST' and request.form['name'] == '陈珍展1':

        s = ['张三', '年龄', '姓名']
        t = {}
        for num in range(1, 6):
            t[str(num)] = s
        data = {}

        data['SUCCESS'] = 'SUCCESS'
        data['data'] = t
    else:
        s = ['张四', '年龄', '姓名', '性别']
        t = {}
        for num in range(1, 6):
            t[str(num)] = s
        data = {}
        data['SUCCESS'] = 'SUCCESS'
        data['data'] = t

    return json.dumps(data, ensure_ascii=False)

@home.route("/saveimage/")
def saveimage():

    if not os.path.exists(app.config["UP_DIR"]):
        os.makedirs(app.config["UP_DIR"])
        os.chmod(app.config["UP_DIR"], "rw")

    return "保存图片ok"
