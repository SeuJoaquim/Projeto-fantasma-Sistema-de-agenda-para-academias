from flask import Blueprint,request, render_template,make_response, redirect,url_for, jsonify, make_response

from api.controllers.authorizationMethods           import admin_required


admin = Blueprint("admin", __name__)

# App Routes
@admin.route("/")
# @admin_required
def main_admin(current_user):
    return render_template("/admin/index.html")



# User Database Routes
@admin.route("/user")
# @admin_required
def user(current_user):
    data = {}
    data["email"]   = current_user.email
    data["name"]    = current_user.name
    return jsonify(data)