from dojos_ninjas_app.config.mysqlconnection import connectToMySQL
from dojos_ninjas_app import DATABASE

class Dojo:
    def __init__(self, data):

        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []
    
    # ineract w/ the DATABASE

    # ======= READ ALL ========
    @classmethod
    def fetch_all_dojos(cls):

        query = """
            SELECT * FROM dojos;
            """
        result = connectToMySQL(DATABASE).query_db(query)
        
        these_dojos = []
        
        for row in result:
            this_dojo = cls(row)

            these_dojos.append(this_dojo)

        print(these_dojos)
        return these_dojos
    
    # ======= SAVE ========
    @classmethod
    def create_dojo(cls, data):

        query = """
            INSERT INTO dojos (name, created_at, updated_at)
            VALUES (%(name)s, NOW() , NOW())
            """
        
        result = connectToMySQL(DATABASE).query_db(query, data)

        return result
    

    # ======= SHOW ONE BY ID ========

    @classmethod
    def get_one_dojo_by_id(cls, data):

        query = """
                SELECT * FROM dojos
                WHERE id = %(id)s;
                """
        result = connectToMySQL(DATABASE).query_db(query,data)
        this_dojo = cls(result[0])
        return this_dojo