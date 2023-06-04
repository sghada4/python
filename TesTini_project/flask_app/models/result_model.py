from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
# from flask import flash
from flask_app.models import user_model
# from datetime import datetime

class Result:
    def __init__(self,data):
        self.id=data['id']
        self.value=data['value']
        self.description=data['description']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']

    #* ********** GET RESULT BY VALUE **********
    @classmethod
    def get_by_value(cls, data): #!READ
        query="SELECT * FROM results WHERE value=%(value)s;"
        result= connectToMySQL(DATABASE).query_db(query,data)

        if len(result) <1:
            return False
        return cls(result[0])
        
    #* ***********GET ALL RESULTS OF SPECIFIC USER***********
    @classmethod
    def get_results_of_user(cls,data): #!READ
        query="""SELECT * FROM users 
                JOIN user_pass_tests ON user_pass_tests.user_id = users.id
                JOIN tests ON user_pass_tests.test_id = tests.id
                JOIN results ON user_pass_tests.result_id = results.id
                WHERE users.id = %(user_id)s;"""
        result= connectToMySQL(DATABASE).query_db(query,data)
        results=[]
        for row in result:

            # fix the result ambiguity 
            # prepare the data for the constructor
            
            result_data = {
                **row,
                'id': row['results.id'],
                'created_at': row['results.created_at'],
                'updated_at': row['results.updated_at']
            }

            this_result = cls(result_data)

            results.append(this_result)
        return results
    
    #* ***********GET RESULT OF SPECIFIC USER FOR SPECIFIC TEST***********
    @classmethod
    def get_result_of_user_for_test(cls,data): #!READ
        query="""SELECT * FROM users 
                JOIN user_pass_tests ON user_pass_tests.user_id = users.id
                JOIN tests ON user_pass_tests.test_id = tests.id
                JOIN results ON user_pass_tests.result_id = results.id
                WHERE user_pass_tests.points = %(points)s AND users.id = %(user_id)s;"""
        result= connectToMySQL(DATABASE).query_db(query,data)
        results=[]
        for row in result:

            # fix the result ambiguity 
            # prepare the data for the constructor
            
            result_data = {
                **row,
                'id': row['results.id'],
                'created_at': row['results.created_at'],
                'updated_at': row['results.updated_at']
            }

            this_result = cls(result_data)

            results.append(this_result)
        return results
    
    #* ***********GET RESULT OF SPECIFIC GROUP FOR SPECIFIC TEST***********
    @classmethod
    def get_result_of_group_for_test(cls,data): #!READ
        query="""SELECT * FROM testini_schema.groups 
                JOIN user_pass_tests ON user_pass_tests.group_id = testini_schema.groups.id
                JOIN tests ON user_pass_tests.test_id = tests.id
                JOIN results ON user_pass_tests.result_id = results.id
                WHERE user_pass_tests.points = %(points)s AND testini_schema.groups.id = %(group_id)s;"""
        result= connectToMySQL(DATABASE).query_db(query,data)
        results=[]
        for row in result:

            # fix the result ambiguity 
            # prepare the data for the constructor
            
            result_data = {
                **row,
                'id': row['results.id'],
                'created_at': row['results.created_at'],
                'updated_at': row['results.updated_at']
            }

            this_result = cls(result_data)

            results.append(this_result)
        return results
    
    #* ***********GET ALL RESULTS OF SPECIFIC USER***********
    @classmethod
    def get_results_of_user(cls,data): #!READ
        query="""SELECT * FROM users 
                JOIN user_pass_tests ON user_pass_tests.user_id = users.id
                JOIN tests ON user_pass_tests.test_id = tests.id
                JOIN results ON user_pass_tests.result_id = results.id
                WHERE users.id = %(user_id)s;"""
        result= connectToMySQL(DATABASE).query_db(query,data)
        results=[]
        for row in result:

            # fix the result ambiguity 
            # prepare the data for the constructor
            
            result_data = {
                **row,
                'id': row['results.id'],
                'created_at': row['results.created_at'],
                'updated_at': row['results.updated_at']
            }

            this_result = cls(result_data)

            results.append(this_result)
        return results