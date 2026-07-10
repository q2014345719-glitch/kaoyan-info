from app import app
from models import db, School, Major
import json
import os



BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)


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


    # 清空旧专业数据

    Major.query.delete()



    count = 0



    # 遍历学校

    for school_name, info in school_data.items():


        # 跳过更新时间

        if school_name == "update_time":

            continue



        # 查找对应学校

        school = School.query.filter_by(
            name=school_name
        ).first()



        # 如果数据库没有学校，跳过

        if not school:

            continue



        majors = info.get(
            "majors",
            []
        )



        for major_info in majors:


            major = Major(

                school_id=school.id,

                name=major_info.get(
                    "name"
                ),

                code=major_info.get(
                    "code"
                ),

                study=major_info.get(
                    "study"
                ),

                years=major_info.get(
                    "years"
                ),

                tuition=major_info.get(
                    "tuition"
                )

            )


            db.session.add(
                major
            )


            count += 1



    db.session.commit()



print(
    f"专业数据导入完成，共导入 {count} 个专业！"
)