from flask_sqlalchemy import SQLAlchemy


# 创建数据库对象
db = SQLAlchemy()


# 学校信息表
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


    # 所在省份
    province = db.Column(
        db.String(50)
    )


    # 所在城市
    city = db.Column(
        db.String(50)
    )


    # 学校类型
    school_type = db.Column(
        db.String(50)
    )


    # 官网
    website = db.Column(
        db.String(200)
    )


    def __repr__(self):

        return f"<School {self.name}>"