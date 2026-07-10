from app import app
from models import db, School
import json
import os


# 项目路径
BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)


# JSON路径
DATA_PATH = os.path.join(
    BASE_DIR,
    "data",
    "school_data.json"
)


# 读取JSON

with open(
    DATA_PATH,
    "r",
    encoding="utf-8"
) as f:

    school_data = json.load(f)



with app.app_context():


    # 清空旧数据

    School.query.delete()


    count = 0


    # 遍历学校

    for name, info in school_data.items():


        # 跳过更新时间

        if name == "update_time":

            continue



        school = School(

            name=info.get(
                "name",
                name
            ),

            city=info.get(
                "city"
            ),

            school_type=info.get(
                "type"
            ),

            website=info.get(
                "website"
            )

        )


        db.session.add(school)


        count += 1



    db.session.commit()



print(
    f"学校数据导入完成，共导入 {count} 所学校！"
)