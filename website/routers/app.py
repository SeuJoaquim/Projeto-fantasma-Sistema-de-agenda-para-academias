from flask import Blueprint,request, render_template,make_response, redirect,url_for, jsonify, make_response

from website.controllers.loginController           import token_required


app = Blueprint("app", __name__)

# App Routes
@app.route("/")
@token_required
def main_app(current_user):
    return render_template("/app/index.html")



# User Database Routes
@app.route("/user")
@token_required
def user(current_user):
    data = {}
    data["email"]   = current_user.email
    data["name"]    = current_user.name
    return jsonify(data)