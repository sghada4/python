from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask_app.models import user_model
# from datetime import datetime

class Group:
    def __init__(self,data):
        self.id=data['id']
        self.name=data['name']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        self.user_id=data['user_id']
        self.creator = user_model.User.get_by_id({'id':self.user_id})


    #* ***********CREATE GROUP***********
    @classmethod
    def save_group(cls, data): #!CREATE
        query="INSERT INTO testini_schema.groups (user_id,name) VALUES (%(user_id)s,%(name)s);"
        # this query will return the id of the new group insert
        return connectToMySQL(DATABASE).query_db(query,data)
    
    #* ***********GET ALL USERS GROUPS WITH DETAILS***********
    @classmethod 
    def get_users_groups(cls, data): #!READ
        query="""SELECT * FROM testini_schema.groups
                WHERE user_id = %(user_id)s
                ORDER BY created_at desc;
                """ 
        results= connectToMySQL(DATABASE).query_db(query, data)
        #organize the results
        groups=[]
        for row in results:
            groups.append(cls(row))
        return groups


    @classmethod 
    def get_users_groups_limit(cls, data): #!READ
        query="""SELECT * FROM testini_schema.groups
                WHERE user_id = %(user_id)s
                ORDER BY created_at desc
                LIMIT 4;
                """ 
        results= connectToMySQL(DATABASE).query_db(query, data)
        #organize the results
        groups=[]
        for row in results:
            groups.append(cls(row))
        return groups
    

    @classmethod 
    def get_users_groups_num(cls, data): #!READ
        query="""SELECT COUNT(*) as num FROM testini_schema.groups
                WHERE user_id = %(user_id)s;
                """ 
        results= connectToMySQL(DATABASE).query_db(query, data)
        #organize the results

        return results[0]
    

    @classmethod 
    def get_other_groups_num(cls, data): #!READ
        query="""SELECT COUNT(*) as num FROM testini_schema.groups
                WHERE user_id != %(user_id)s;
                """ 
        results= connectToMySQL(DATABASE).query_db(query, data)
        #organize the results

        return results[0]
    


    #* ***********GET ALL OTHERS GROUPS WITH DETAILS***********
    @classmethod 
    def get_others_groups_limit(cls, data): #!READ
        query="""  SELECT * FROM testini_schema.groups
                WHERE testini_schema.groups.user_id != %(user_id)s
                ORDER BY created_at desc 
                LIMIT 4;
                """ 
        results= connectToMySQL(DATABASE).query_db(query, data)
        #organize the results
        groups=[]
        for row in results:
            groups.append(cls(row))
        return groups
    


    

    @classmethod 
    def get_others_groups_super_user(cls, data): #!READ
        query="""  SELECT * FROM testini_schema.groups
                WHERE testini_schema.groups.user_id != %(user_id)s
                ORDER BY created_at desc;
                """ 
        results= connectToMySQL(DATABASE).query_db(query, data)
        #organize the results
        groups=[]
        for row in results:
            groups.append(cls(row))
        return groups
    
    #* ***********GET ONE GROUP BY ID***********
    @classmethod
    def get_by_id_group(cls,data): #!READ
        query="SELECT * FROM testini_schema.groups WHERE id=%(id)s;"
        result= connectToMySQL(DATABASE).query_db(query,data)
        if len(result)<1:
            return []
        return cls(result[0])

    #* ***********UPDATE GROUP***********
    @classmethod
    def update_group(cls,data): #!UPDATE//EDIT
        query="""UPDATE testini_schema.groups 
                SET name=%(name)s
                WHERE id=%(id)s;"""
        return connectToMySQL(DATABASE).query_db(query,data)
    
    #* ***********SELECT JOINED GROUPS***********
    @classmethod
    def joined_groups(cls,data): #!READ
        query="""SELECT * FROM testini_schema.groups
                JOIN joins ON testini_schema.groups.id = joins.group_id
                JOIN users ON joins.user_id = users.id
                WHERE joins.user_id=%(user_id)s;
            """
        result = connectToMySQL(DATABASE).query_db(query,data)
        if len(result)<1:
            return []
        
        groups=[]
        for row in result:
            
            groups.append(cls(row))
        return groups
    
    @classmethod
    def joined_groups_num(cls,data): #!READ
        query="""SELECT count(*) as num FROM testini_schema.groups
                JOIN joins ON testini_schema.groups.id = joins.group_id
                JOIN users ON joins.user_id = users.id
                WHERE joins.user_id=%(user_id)s;
            """
        result = connectToMySQL(DATABASE).query_db(query,data)
        if len(result)<1:
            return []
    
        return result[0]     


    @classmethod
    def other_groups_num(cls,data): #!READ
        query="""  SELECT count(*) as num FROM testini_schema.groups
                WHERE testini_schema.groups.id NOT IN ( SELECT group_id FROM joins WHERE joins.user_id = %(user_id)s );
                """ 
        result = connectToMySQL(DATABASE).query_db(query,data)
        if len(result)<1:
            return []
    
        return result[0]    
    #* ***********JOIN A GROUP***********
    @classmethod
    def join_group(cls,data): #!CREATE
        query="""INSERT INTO joins (user_id, group_id)
                VALUES (%(user_id)s,%(group_id)s);
            """
        return connectToMySQL(DATABASE).query_db(query,data)

    #* ***********CANCEL A JOINED GROUP***********
    @classmethod
    def cancel_group(cls,data): #!DELETE
        query="DELETE FROM joins WHERE user_id=%(user_id)s AND group_id=%(group_id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)
    
    @classmethod
    def delete_group(cls,data): #!DELETE
        query="DELETE FROM testini_schema.groups WHERE id=%(id)s ;"
        return connectToMySQL(DATABASE).query_db(query,data)

    #* ***********SELECT ONE JOINED GROUP***********
    @classmethod
    def one_joined_group(cls,data): #!READ
        query="""SELECT * FROM testini_schema.groups
                JOIN joins ON groups.id = joins.group_id
                JOIN users ON joins.user_id = users.id
                WHERE joins.group_id=%(group_id)s AND joins.user_id=%(user_id)s;
            """
        result= connectToMySQL(DATABASE).query_db(query,data)
        if len(result)<1:
            return []
        
        return result[0]
    

    #* ***********GET ALL OTHERS GROUPS WITH DETAILS FOR USER***********
    @classmethod 
    def get_others_groups_user(cls, data): #!READ
        query="""  SELECT * FROM testini_schema.groups
                WHERE testini_schema.groups.id NOT IN ( SELECT group_id FROM joins WHERE joins.user_id = %(user_id)s );
                """ 
        results= connectToMySQL(DATABASE).query_db(query, data)
        #organize the results
        groups=[]
        for row in results:
            groups.append(cls(row))
        return groups


    #* ***********GET ALL OTHERS GROUPS WITH DETAILS FOR SUPER USER***********
    @classmethod 
    def get_other_users_groups(cls, data): #!READ
        query="""  SELECT * FROM testini_schema.groups
                WHERE testini_schema.groups.id != %(id)s );
                """ 
        results= connectToMySQL(DATABASE).query_db(query, data)
        #organize the results
        groups=[]
        for row in results:
            groups.append(cls(row))
        return groups


    #* ***********VALIDATE GROUP*********** 
    @staticmethod #!VALIDATION
    def validate_group(data): 
        is_valid = True

        if len(data['name'])<0:
            flash("Name must be more than 0 characters!","group")
            is_valid = False
            
        return is_valid
    


