from flask import Flask, render_template, request, jsonify
from models import db, School
import os


app = Flask(__name__)


# 数据库配置

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)


db_path = os.path.join(
    BASE_DIR,
    "database",
    "kaoyan.db"
)


app.config["SQLALCHEMY_DATABASE_URI"] = (
    "sqlite:///" + db_path
)


app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


# 初始化数据库

db.init_app(app)



# 首页

@app.route("/")
def home():

    return render_template(
        "index.html"
    )



# 搜索学校

@app.route(
    "/search",
    methods=["POST"]
)
def search():


    school_name = request.form.get(
        "school",
        ""
    ).strip()



    # 数据库查询

    school = School.query.filter_by(
        name=school_name
    ).first()



    return render_template(
        "index.html",
        school=school
    )



# 搜索提示

@app.route("/suggest")
def suggest():


    keyword = request.args.get(
        "q",
        ""
    ).strip()



    schools = School.query.filter(
        School.name.like(
            f"%{keyword}%"
        )
    ).all()



    result = [
        s.name
        for s in schools
    ]


    return jsonify(result)



# 创建数据库测试

@app.route("/test_db")
def test_db():

    count = School.query.count()

    return f"数据库共有 {count} 所学校"



if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )