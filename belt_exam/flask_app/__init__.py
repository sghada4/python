from flask import Flask
app = Flask(__name__)
app.secret_key = "red belt key"
DATABASE = "shows_schema"