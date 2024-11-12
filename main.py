from app import Create_app
from flask import session
from app.models import db

app = Create_app()

@app.route("/")
def func():
    print(session)
    return f"{session}"

if __name__=="__main__":
    with app.app_context():
        db.create_all()
    app.run()