from flask import Flask, render_template, request, jsonify
from models import db, School
import json
import os


app = Flask(__name__)


# ==========================
# 数据库配置
# ==========================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


app.config["SQLALCHEMY_DATABASE_URI"] = (
    "sqlite:///" +
    os.path.join(
        BASE_DIR,
        "database",
        "kaoyan.db"
    )
)


app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


# 初始化数据库

db.init_app(app)



# ==========================
# 原来的JSON数据
# ==========================

DATA_PATH = os.path.join(
    BASE_DIR,
    "data",
    "school_data.json"
)


with open(DATA_PATH, "r", encoding="utf-8") as f:
    school_data = json.load(f)



update_time = school_data.get("update_time")


if "update_time" in school_data:
    school_data.pop("update_time")



# ==========================
# 首页
# ==========================

@app.route("/")
def home():

    return render_template(
        "index.html",
        update_time=update_time
    )



# ==========================
# 搜索学校
# ==========================

@app.route("/search", methods=["POST"])
def search():

    school = request.form.get(
        "school",
        ""
    ).strip()


    info = school_data.get(
        school
    )


    return render_template(
        "index.html",
        school=school,
        info=info,
        update_time=update_time
    )



# ==========================
# 搜索建议
# ==========================

@app.route("/suggest")
def suggest():

    keyword = request.args.get(
        "q",
        ""
    ).strip()


    result = [
        s for s in school_data
        if keyword in s
    ]


    return jsonify(result)



# ==========================
# 创建数据库表（首次运行）
# ==========================

@app.route("/init_db")
def init_db():

    with app.app_context():

        db.create_all()


    return "数据库初始化成功"



# ==========================
# 启动
# ==========================

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )