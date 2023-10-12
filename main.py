from flask import Flask
from public import public
from admin import admin
from user import user
from homecook import homecook

app=Flask(__name__)

app.secret_key="secret_key"

app.register_blueprint(public)
app.register_blueprint(admin,url_prefix="/admin")
app.register_blueprint(user,url_prefix="/user")
app.register_blueprint(homecook,url_prefix="/homecook")

app.run(debug=True,port=5010)