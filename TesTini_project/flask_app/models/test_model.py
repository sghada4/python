from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
# from flask import flash
from flask_app.models import module_model,user_pass_tests_model, user_model
# from datetime import datetime

class Test:
    def __init__(self,data):
        self.id=data['id']
        self.name=data['name']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        self.module_id=data['module_id']
        self.belong = module_model.Module.get_by_id({'id':self.module_id})

    #* ***********GET Test OF SPECIFIC MODULE***********
    @classmethod
    def get_test_by_module(cls,data): #!READ
        query="SELECT * FROM tests WHERE module_id=%(module_id)s;"
        result= connectToMySQL(DATABASE).query_db(query,data)
        tests=[]
        for row in result:
            tests.append(cls(row))
        return tests
    
    #* ********** GET TEST BY ID **********
    @classmethod
    def get_test_by_id(cls, data): #!READ
        query="SELECT * FROM tests WHERE id=%(id)s;"
        result= connectToMySQL(DATABASE).query_db(query,data)

        if len(result) <1:
            return False
        return cls(result[0])
    
    #* ********** GET ALL TESTS OF A SPECIFIC MODULE **********
    @classmethod
    def get_all_tests_module(cls,data): #!READ
        query="""SELECT * FROM modules 
                JOIN tests ON modules.id = tests.module_id
                WHERE modules.id =%(id)s"""
        result= connectToMySQL(DATABASE).query_db(query,data)

        tests=[]
        for row in result:
            this_module = module_model.Module(row)
            # fix the test ambiguity 
            # prepare the data for the constructor
            
            test_data = {
                **row,
                'id': row['tests.id'],
                'name': row['tests.name'],
                'created_at': row['tests.created_at'],
                'updated_at': row['tests.updated_at']
            }

            this_test = cls(test_data)
            this_test.belong = this_module
            tests.append(this_test)
        return tests
    
    #* ********** CREATE TEST **********
    @classmethod
    def save_test(cls, data): #!CREATE
        query = """INSERT INTO tests (name, module_id)
        VALUES (%(name)s, %(module_id)s);"""
        return connectToMySQL(DATABASE).query_db(query,data)