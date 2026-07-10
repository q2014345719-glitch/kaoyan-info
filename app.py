from flask import Flask, render_template, request, jsonify
import json
import os


app = Flask(__name__)


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


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



@app.route("/")
def home():

    return render_template(
        "index.html",
        update_time=update_time
    )



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



if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )