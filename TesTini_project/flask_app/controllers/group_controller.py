from flask_app import app
from flask import render_template,request, redirect, session,flash
from flask_app.models.group_model import Group
from flask_app.models.module_model import Module
from flask_app.models.user_model import User

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)



