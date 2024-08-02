from users_app.config.mysqlconnection import connectToMySQL
from users_app import DATABASE

class User:
    def __init__(self, data):
        self.id = data['id'],
        self.first_name = data['first_name'],
        self.last_name = data['last_name'],
        self.email = data['email'],
        self.created_at = data['created_at'],
        self.updated_at = data['updated_at']
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users"
        users_from_db = connectToMySQL(DATABASE).query_db(query)
        users = []
        for user in users_from_db:
            one_user = cls(user)
            users.append(one_user)
            print(user)
        return users
    
    @classmethod
    def save(cls,data):
        query = "Insert INTO users (first_name,last_name,email,created_at,updated_at) VALUES(%(first_name)s,%(last_name)s,%(email)s,NOW(),NOW());"
        user_id = connectToMySQL(DATABASE).query_db(query,data)
        return user_id

