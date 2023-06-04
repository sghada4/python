from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
# from flask import flash
# from flask_app.models import user_model
# from datetime import datetime

class Response:
    def __init__(self,data):
        self.id=data['id']
        self.response=data['response']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']

    #* ********** GET RESPONSE BY ID **********
    @classmethod
    def get_by_id(cls, data): #!READ
        query="SELECT * FROM responses WHERE id=%(id)s;"
        result= connectToMySQL(DATABASE).query_db(query,data)

        if len(result) <1:
            return False
        return cls(result[0])
        
    #* ***********GET RESPONSES OF SPECIFIC QUESTION***********
    @classmethod
    def get_responses_of_quetion(cls,data): #!READ
        query="""SELECT * FROM questions
                JOIN responses_has_questions ON responses_has_questions.question_id = questions.id
                JOIN responses ON responses.id = responses_has_questions.response_id
                WHERE questions.id =%(question_id)s;"""
        result= connectToMySQL(DATABASE).query_db(query,data)
        responses=[]
        for row in result:

            # fix the response ambiguity 
            # prepare the data for the constructor
            
            response_data = {
                **row,
                'id': row['responses.id'],
                'created_at': row['responses.created_at'],
                'updated_at': row['responses.updated_at']
            }

            this_response = cls(response_data)

            responses.append(this_response)
        return responses