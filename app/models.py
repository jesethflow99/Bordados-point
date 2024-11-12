from flask_sqlalchemy import SQLAlchemy


db= SQLAlchemy()

class Usuario(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    Nombre_Usuario=db.Column(db.String(50),nullable=False)
    Contraseña=db.Column(db.String,nullable=False)
    
    def __init__(self,Nombre_Usuario,Contraseña):
        self.Nombre_Usuario=Nombre_Usuario
        self.Contraseña=Contraseña
        
    def __repr__(self) -> str:
        return f"Usuario: {self.Nombre_Usuario}"