from flask import Blueprint,request, render_template,make_response, redirect


router = Blueprint("router", __name__)

@router.route("/", methods=["GET"])
def home():
    return render_template("home.html")

@router.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
    if request.method == 'POST':
       user = request.form['nm']
       resp = make_response(redirect("/getcookie"))
       resp.set_cookie('userID', user)
       return resp

@router.route('/getcookie')
def getcookie():
   name = request.cookies.get('userID')
   return '<h1>welcome ' + name + '</h1>'
