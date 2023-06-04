from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
# from flask import flash
# from flask_app.models import module_model
# from datetime import datetime

class User_pass_tests:
    def __init__(self,data):
        self.id=data['id']
        self.user_id=data['user_id']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        self.test_id=data['test_id']
        self.points=data['points']
        self.result_id=data['result_id']
        self.group_id=data['group_id']

        
