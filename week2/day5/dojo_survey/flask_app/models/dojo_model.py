from flask_app.config import mysqlconnection
from flask_app import DATABASE
from flask import flash
class Dojo:
    def __init__(self,data):
        self.id=data['id']
        self.name=data['name']
        self.location=data['location']
        self.language=data['language']
        self.comment=data['comment']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
    
    @classmethod
    def get_all(cls):
        query = """
                SELECT * FROM dojo;
        """
        result =mysqlconnection.MySQLConnection(DATABASE).query_db(query)
        all_dojos=[]
        for row in result:
            all_dojos.append(cls(row))
        
        return all_dojos
    
    @classmethod
    def save(cls, data):
        query = """
                INSERT INTO dojo (name, location, language, comment) 
                Values (%(name)s, %(location)s, %(language)s, %(comment)s);
                """
        return mysqlconnection.MySQLConnection(DATABASE).query_db(query, data)

    @staticmethod
    def validate_dojo(dojo):
        is_valid = True # we assume this is true
        if len(dojo['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        
        if len(dojo['comment']) < 3:
            flash("comment is required.")
            is_valid = False
        return is_valid