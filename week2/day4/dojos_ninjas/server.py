from flask import Flask  # Import Flask to allow us to create our app
from dojos_ninjas_app import app
from dojos_ninjas_app.controllers import dojos_controller
from dojos_ninjas_app.controllers import ninjas_controller


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True, port=5003)    # Run the app in debug mode.



