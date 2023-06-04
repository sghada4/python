from flask import Flask  # Import Flask to allow us to create our app
from flask_app import app
from flask_app.controllers import group_controller, module_controller, question_controller, response_controller, result_controller,super_user_controller, test_controller


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.



