from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

with open("data/school_data.json", "r", encoding="utf-8") as f:
    school_data = json.load(f)

update_time = school_data.get("update_time")
school_data.pop("update_time", None)

@app.route("/")
def home():
    return render_template("index.html", update_time=update_time)

@app.route("/search", methods=["POST"])
def search():
    school = request.form.get("school", "").strip()
    info = school_data.get(school)
    return render_template("index.html", school=school, info=info, update_time=update_time)

@app.route("/suggest")
def suggest():
    keyword = request.args.get("q", "").strip()
    result = [s for s in school_data if keyword in s]
    return jsonify(result)   # 改这一行

if __name__ == "__main__":
    app.run(debug=True)