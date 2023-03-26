from flask import Flask, render_template, request
import os
import utils

app = Flask(__name__)


@app.route("/")
def index_route():
    return render_template("index.html")


@app.route("/forgot")
def forgot_route():
    return render_template("forgot.html")


@app.route("/main")
def main_page():
    return render_template("main.html")


@app.route("/add_food")
def add_food():
    return render_template("addfood.html")


@app.route("/add_train")
def add_train():
    return render_template("addzan.html")


@app.route("/api/login_pass")
def login_pass():
    if not request.json:
        raise Exception
    data = request.json
    return utils.check_user(data["username"], data["password"])


@app.route("/api/register")
def register():
    if not request.json:
        raise Exception
    data = request.json
    return utils.register(data["username"], data["password"])


@app.route("/api/change_password", methods=['POST'])
def change_password():
    if not request.json:
        raise Exception
    data = request.json
    return utils.change_password(data["username"], data["password"])


@app.route("/api/add_food", methods=['POST'])
def api_add_food():
    if not request.json:
        raise Exception
    data = request.json
    return utils.add_food(data["id"], data["food"])


@app.route("/api/add_train", methods=['POST'])
def api_add_train():
    if not request.json:
        raise Exception
    data = request.json
    return utils.add_train(data["id"], data["train"])


@app.route("/api/remove_train", methods=['POST'])
def api_remove_train():
    if not request.json:
        raise Exception
    data = request.json
    return utils.remove_train(data["id"], data["train"])


@app.route("/api/remove_food", methods=['POST'])
def api_remove_food():
    if not request.json:
        raise Exception
    data = request.json
    return utils.remove_food(data["id"], data["food"])


@app.route("/api/get_trains", methods=['POST'])
def api_get_trains():
    if not request.json:
        raise Exception
    data = request.json
    return utils.get_trains(data["id"])


@app.route("/api/get_food", methods=['POST'])
def api_get_food():
    if not request.json:
        raise Exception
    data = request.json
    return utils.get_food(data["id"])


if __name__ == "__main__":
    app.run("0.0.0.0")
