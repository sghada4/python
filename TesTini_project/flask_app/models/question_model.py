from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
# from flask import flash
from flask_app.models import test_model
# from datetime import datetime

class Question:
    def __init__(self,data):
        self.id=data['id']
        self.statement=data['statement']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        self.test_id=data['test_id']
        self.belong = test_model.Test.get_test_by_id({'id':self.test_id})

    #* ***********GET QUESTIONS OF SPECIFIC TEST***********
    @classmethod
    def get_questions_of_test(cls,data): #!READ
        query="""SELECT * FROM questions 
                JOIN tests ON questions.test_id = tests.id
                WHERE test_id=%(test_id)s;"""
        result= connectToMySQL(DATABASE).query_db(query,data)
        questions=[]
        for row in result:
            questions.append(cls(row))
        return questions