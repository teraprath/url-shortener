from flask import Flask, render_template, redirect, url_for, request
import database

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form["url"]
        database.insert(url)
    urls = database.fetchall()
    return render_template("pages/index.html", urls=urls)

@app.route("/<string:id>")
def short(id):
    url = database.fetchone(id)
    if url:
        return redirect(url[1])
    return redirect(url_for("index"))

@app.route("/delete/<string:id>")
def delete(id):
    url = database.fetchone(id)
    if url:
        database.delete(url[0])
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(port=5500, debug=True)