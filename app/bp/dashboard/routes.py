from flask import Blueprint,request,render_template,redirect,url_for,session
import app.bp.auth.routes
from app.models import Usuario,db


dashboard=Blueprint("dashboard",__name__,url_prefix="/dashboard")

@dashboard.route("/inicio")
def index():

    if session:
        mess=True
        nombre=session["Nombre_usuario"]
        return render_template("index.html",nombre =nombre)
    else:
        mess=False
        return redirect(url_for("auth.login"))
    