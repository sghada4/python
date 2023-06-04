from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
import re	  
from flask_app.models import test_model,user_pass_tests_model


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__(self,data):
        self.id=data['id']
        self.first_name=data['first_name']
        self.last_name=data['last_name']
        self.email=data['email']
        self.password=data['password']
        self.role=data['role']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        self.belong_test=[]
        self.pass_test=[]

    #* ********** CREATE USER **********
    @classmethod
    def save_user(cls, data): #!CREATE//INSERT
        query = """INSERT INTO users (first_name, last_name, email, password, role)
        VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s,%(role)s);"""
        return connectToMySQL(DATABASE).query_db(query,data)
    
    #* ********** CREATE SUPER USER **********
    # @classmethod
    # def save_super_user(cls, data): #!CREATE//INSERT
    #     query = """INSERT INTO users (first_name, last_name, email, password,role)
    #     VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, %(role)s);"""
    #     return connectToMySQL(DATABASE).query_db(query,data)
    
    #* ********** GET USER BY HIS EMAIL **********
    @classmethod
    def get_by_email(cls, data): #!READ
        query="SELECT * FROM users WHERE email=%(email)s;"
        result= connectToMySQL(DATABASE).query_db(query,data)

        if len(result) <1:
            return False
        return cls(result[0])

    #* ********** GET USER BY HIS ID **********
    @classmethod
    def get_by_id(cls, data): #!READ
        query="SELECT * FROM users WHERE id=%(id)s;"
        result= connectToMySQL(DATABASE).query_db(query,data)

        if len(result) <1:
            return False
        return cls(result[0])
    



    #* ********** GET ALL TESTS OF A SPECIFIC USER **********
    @classmethod
    def get_all_tests_user(cls,data): #!READ
        query="""SELECT * FROM tests 
                JOIN user_pass_tests ON tests.id = user_pass_tests.test_id
                JOIN users ON users.id = user_pass_tests.user_id
                WHERE users.id =%(id)s"""
        result= connectToMySQL(DATABASE).query_db(query,data)
        if not result:
            return []
        tests=[]
        for row in result:
            this_test = test_model.Test(row)
            user_pass_tests_data={
                **row,
                'id': row['user_pass_tests.id'],
                'created_at':row['created_at'],
                'updated_at':row['updated_at']
            }
            pass_tests=user_pass_tests_model.User_pass_tests(user_pass_tests_data)
            # fix the test ambiguity 
            # prepare the data for the constructor
            
            user_data = {
                **row,
                'id': row['users.id'],
                'created_at': row['users.created_at'],
                'updated_at': row['users.updated_at']
            }
            user=cls(user_data)
            user.belong_test.append(this_test)
            user.pass_test.append(pass_tests)
            tests.append(user)
        return tests



    
    #* ********** CHECK REGISTER INFORMATION **********
    #validate user
    @staticmethod #!VALIDATION
    def validate_user(data):
        is_valid = True

        if len(data['first_name'])<2:
            flash("First Name must be more than 2 characters!","register")
            is_valid = False
        if len(data['last_name'])<2:
            flash("Last Name must be more than 2 characters!","register")
            is_valid = False
        if not EMAIL_REGEX.match(data['email']): 
            flash("Email must be valid !","register")
            is_valid = False
        elif User.get_by_email({'email':data['email']}):
            flash("Email already exist !","register")
            is_valid = False
        if len(data['password'])<6:
            flash("Password must be more than 6 characters!","register")
            is_valid = False
        elif data['password']!=data['confirm_password']:
            flash("Passwords do not match!","register")
            is_valid = False

        return is_valid
    







    