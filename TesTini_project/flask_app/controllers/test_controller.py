from flask_app import app
from flask import render_template,request, redirect, session,flash
from flask_app.models.user_model import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

