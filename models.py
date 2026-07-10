from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class School(db.Model):

    __tablename__ = "schools"


    id = db.Column(
        db.Integer,
        primary_key=True
    )


    name = db.Column(
        db.String(100),
        nullable=False
    )


    city = db.Column(
        db.String(100)
    )


    school_type = db.Column(
        db.String(50)
    )


    website = db.Column(
        db.String(200)
    )



    # 一个学校对应多个专业

    majors = db.relationship(
        "Major",
        backref="school",
        lazy=True
    )




class Major(db.Model):

    __tablename__ = "majors"


    id = db.Column(
        db.Integer,
        primary_key=True
    )


    # 所属学校

    school_id = db.Column(
        db.Integer,
        db.ForeignKey("schools.id")
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