from users_app import app
from flask import Flask  # Import Flask to allow us to create our app
from users_app.controllers import users_controller


if __name__ == '__main__':
    app.run(debug=True)
