from flask_app import app
#! Always remember to import all routes here ( all controllers)
from flask_app.controllers import show_controller
from flask_app.controllers import user_controller
if __name__ == '__main__':
    app.run(debug=True)