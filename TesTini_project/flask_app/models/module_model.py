from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
# from flask import flash
# from flask_app.models import user_model
# from datetime import datetime

class Module:
    def __init__(self,data):
        self.id=data['id']
        self.name=data['name']
        self.description=data['description']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        self.users=[]

    #* ********** GET MODULE BY ID **********
    @classmethod
    def get_by_id(cls, data): #!READ
        query="SELECT * FROM modules WHERE id=%(id)s;"
        result= connectToMySQL(DATABASE).query_db(query,data)

        if len(result) <1:
            return False
        return cls(result[0])
        
    #* ********** GET ALL MODULES **********
    #* ********** GET ALL MODULES **********
    @classmethod
    def get_all_modules(cls): #!READ
        query="SELECT * FROM modules;"
        result= connectToMySQL(DATABASE).query_db(query)

        modules=[]
        for row in result:
            modules.append(cls(row))
        return modules
    
    

    # @classmethod 
    # def get_info_one_module(cls, data): #!READ
    #     query=""" SELECT * FROM testini_schema.modules as modules
    #             JOIN testini_schema.tests as tests ON modules.id=tests.module_id
    #             JOIN testini_schema.user_pass_tests as pass_test ON tests.id=pass_test.test_id
    #             JOIN testini_schema.users as users ON users.id=pass_test.user_id
    #             LEFT JOIN testini_schema.results as results  on pass_test.result_id=results.id
                
    #             WHERE pass_test.group_id=%(group_id)s%;
    #             """ 
    #     results= connectToMySQL(DATABASE).query_db(query, data)
    #     if not results:
    #         return []
    #     #organize the results
    #     modules=[]
    #     for row in results:
    #         modules.append(cls(row))

    #     return modules
