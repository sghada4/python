from dojos_ninjas_app.config.mysqlconnection import connectToMySQL
from dojos_ninjas_app import DATABASE
from dojos_ninjas_app.models import dojo_model

class Ninja:
    def __init__(self, data):

        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']
        self.below = []

    @classmethod
    def fetch_all_ninjas(cls):

        query = """
            SELECT * FROM ninjas
            LEFT JOIN dojos ON ninjas.dojo_id = dojos.id;
            """
        result = connectToMySQL(DATABASE).query_db(query)
        
        these_ninjas = []
        
        print(result)

        for row in result:
            this_ninja = cls(row)

            # fix the dojo ambiguity 
            # prepare the data for the constructor
            dojo_data = {
                'id': row['dojos.id'],
                'name': row['name'],
                'created_at': row['dojos.created_at'],
                'updated_at': row['dojos.updated_at']
            }

            this_dojo = dojo_model.Dojo(dojo_data)
            this_ninja.below = this_dojo

            these_ninjas.append(this_ninja)

        return these_ninjas
    
     # ======= SAVE ========
    @classmethod
    def create_ninja(cls, data):

        query = """
            INSERT INTO ninjas (first_name, last_name,age,dojo_id, created_at, updated_at)
            VALUES (%(first_name)s,%(last_name)s,%(age)s,%(dojo_id)s, NOW() , NOW())
            """
        
        result = connectToMySQL(DATABASE).query_db(query, data)

        return result
    
    @classmethod
    def fetch_ninjas_dojo(cls, data):

        query = """
            SELECT * FROM ninjas
            LEFT JOIN dojos ON ninjas.dojo_id = dojos.id
            WHERE dojos.id = %(id)s;
            """
        result = connectToMySQL(DATABASE).query_db(query, data)
        
        these_ninjas = []
        
        print(result)

        for row in result:
            this_ninja = cls(row)

            # fix the dojo ambiguity 
            # prepare the data for the constructor
            dojo_data = {
                'id': row['dojos.id'],
                'name': row['name'],
                'created_at': row['dojos.created_at'],
                'updated_at': row['dojos.updated_at']
            }

            this_dojo = dojo_model.Dojo(dojo_data)
            this_ninja.below = this_dojo

            these_ninjas.append(this_ninja)

        return these_ninjas