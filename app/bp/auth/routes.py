from flask import Blueprint,request,render_template,redirect,url_for,session
from app.models import Usuario,db
from app.encrypt import hashear_password,verificar_contraseña

auth=Blueprint("auth",__name__,url_prefix="/auth")

@auth.route("/login",methods=["POST","GET"])
def login():
    if request.method=="POST":
        nombre= request.form.get("nombre")
        contasena=request.form.get("contrasena")
        
        usuario=Usuario.query.filter(Usuario.Nombre_Usuario==nombre).first()
        
        if usuario and verificar_contraseña(contasena,usuario.Contraseña):
            session["usuario_id"]=usuario.id
            session["Nombre_usuario"]=usuario.Nombre_Usuario
            print(session)
            return redirect(url_for("dashboard.index"))
    
    return render_template("login.html")

@auth.route("/logout")
def logout():
    session.pop('usuario_id', None)
    session.pop('Nombre_usuario', None)
    print(session)
    return "deslogear Usuario"

@auth.route("/register",methods=["POST","GET"])
def register():
    if request.method== "POST":
        nombre= request.form.get("nombre")
        contasena=request.form.get("contrasena")
        
        hash_cont=hashear_password(contasena)
        usuario=Usuario.query.filter(Usuario.Nombre_Usuario==nombre).first()
        if usuario:
            return  "el usuario ya existe"
        nuevo_usuario= Usuario(nombre,hash_cont)
        db.session.add(nuevo_usuario)
        db.session.commit()
        print(session)
        return redirect(url_for("auth.login"))
    
    return render_template("register.html")

