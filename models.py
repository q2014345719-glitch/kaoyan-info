from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



# ======================
# 学校表
# ======================

class School(db.Model):

    __tablename__ = "schools"


    id = db.Column(
        db.Integer,
        primary_key=True
    )


    # 学校名称
    name = db.Column(
        db.String(100),
        nullable=False
    )


    # 城市
    city = db.Column(
        db.String(100)
    )


    # 学校类型
    school_type = db.Column(
        db.String(50)
    )


    # 办学层次
    level = db.Column(
        db.String(100)
    )


    # 官网
    website = db.Column(
        db.String(200)
    )


    # 专业关系

    majors = db.relationship(
        "Major",
        backref="school",
        lazy=True,
        cascade="all, delete"
    )





# ======================
# 专业表
# ======================

class Major(db.Model):

    __tablename__ = "majors"


    id = db.Column(
        db.Integer,
        primary_key=True
    )


    # 所属学校

    school_id = db.Column(
        db.Integer,
        db.ForeignKey(
            "schools.id"
        )
    )


    # 专业名称

    name = db.Column(
        db.String(100)
    )


    # 专业代码

    code = db.Column(
        db.String(20)
    )


    # 学习方式

    study = db.Column(
        db.String(50)
    )


    # 学制

    years = db.Column(
        db.Integer
    )


    # 学费

    tuition = db.Column(
        db.String(100)
    )


    # 招生人数

    plan = db.Column(
        db.Integer
    )


    # 推免人数

    tuimian = db.Column(
        db.Integer
    )


    # 初试科目

    subjects = db.Column(
        db.Text
    )