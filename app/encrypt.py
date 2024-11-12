import bcrypt

def hashear_password(password):
    salt = bcrypt.gensalt()
    hasshed_password=bcrypt.hashpw(password.encode(),salt)

    return hasshed_password

def verificar_contraseña(password,hashed_pasword):
    try:
        if bcrypt.checkpw(password.encode(),hashed_pasword):
           return True
        else:
            return False
    except Exception as e:
        print(e)