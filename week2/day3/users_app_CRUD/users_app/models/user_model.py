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
        return users
    
    @classmethod
    def save(cls,data):
        query = "INSERT INTO users (first_name,last_name,email,created_at,updated_at) VALUES(%(first_name)s,%(last_name)s,%(email)s,NOW(),NOW());"
        user_id = connectToMySQL(DATABASE).query_db(query,data)
        return user_id

    @classmethod
    def get_one_by_id(cls, data):

        query = """
                SELECT * FROM users
                WHERE id = %(id)s;
                """
        result = connectToMySQL(DATABASE).query_db(query,data)
        user = cls(result[0])
        return user
    
    @classmethod
    def edit(cls,data):
        query = "UPDATE users SET first_name = %(first_name)s,last_name = %(last_name)s,email = %(email)s, updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)
    
    @classmethod
    def delete(cls,data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)
