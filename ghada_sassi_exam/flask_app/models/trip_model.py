from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask_app.models import user_model
from datetime import datetime

class Trip:
    def __init__(self,data):
        self.id=data['id']
        self.destination=data['destination']
        self.start_date=data['start_date']
        self.end_date=data['end_date']
        self.plan=data['plan']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        self.user_id=data['user_id']
        self.creator = user_model.User.get_by_id({'id':self.user_id})


    #* ***********CREATE TRIP***********
    @classmethod
    def save_trip(cls, data): #!CREATE
        query="INSERT INTO trips (user_id,destination,start_date,end_date,plan) VALUES (%(user_id)s,%(destination)s,%(start_date)s,%(end_date)s,%(plan)s);"
        # this query will return the id of the new trip insert
        return connectToMySQL(DATABASE).query_db(query,data)
    
    #* ***********GET ALL USERS TRIPS WITH DETAILS***********
    #get all trips
    @classmethod 
    def get_users_trips(cls, data): #!READ
        query="""SELECT * FROM trips
                WHERE user_id = %(user_id)s 
                ORDER BY trips.created_at DESC;
                """ 
        results= connectToMySQL(DATABASE).query_db(query, data)
        #organize the results
        trips=[]
        for row in results:
            trips.append(cls(row))
        return trips

    #* ***********GET ALL PEOPLES TRIPS WITH DETAILS***********
    #get all trips
    @classmethod 
    def get_peoples_trips(cls, data): #!READ
        query="""  SELECT * FROM trips
                WHERE trips.user_id != %(user_id)s AND trips.id NOT IN ( SELECT trip_id FROM joins WHERE joins.user_id = %(user_id)s )
                ORDER BY trips.created_at DESC;
                """ 
        results= connectToMySQL(DATABASE).query_db(query, data)
        #organize the results
        trips=[]
        for row in results:
            trips.append(cls(row))
        return trips
    
    #* ***********GET ONE TRIP BY ID***********
    #get one trip by id
    @classmethod
    def get_by_id_trip(cls,data): #!READ
        query="SELECT * FROM trips WHERE id=%(id)s;"
        result= connectToMySQL(DATABASE).query_db(query,data)
        if len(result)<1:
            return False
        return cls(result[0])

    #* ***********UPDATE TRIP***********
    @classmethod
    def update_trip(cls,data): #!UPDATE//EDIT
        query="""UPDATE trips 
                SET destination=%(destination)s,start_date=%(start_date)s,end_date=%(end_date)s,plan=%(plan)s
                WHERE id=%(id)s;"""
        return connectToMySQL(DATABASE).query_db(query,data)
    
    #* ***********DELETE TRIP***********
    @classmethod
    def delete_trip(cls,data): #!DELETE
        query="DELETE FROM trips WHERE id=%(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)

    #* ***********SELECT JOINED TRIPS***********
    @classmethod
    def joined_trips(cls,data): #!READ
        query="""SELECT * FROM trips
                JOIN joins ON trips.id = joins.trip_id
                JOIN users ON joins.user_id = users.id
                WHERE joins.user_id=%(user_id)s
                ORDER BY trips.created_at;
            """
        result = connectToMySQL(DATABASE).query_db(query,data)
        if len(result)<1:
            return []
        
        trips=[]
        for row in result:
            
            trips.append(cls(row))
        return trips
        


    
    #* ***********JOIN A TRIP***********
    @classmethod
    def join_trip(cls,data): #!CREATE
        query="""INSERT INTO joins (user_id, trip_id)
                VALUES (%(user_id)s,%(trip_id)s);
            """
        return connectToMySQL(DATABASE).query_db(query,data)

    #* ***********CANCEL A JOINED TRIP***********
    @classmethod
    def cancel_trip(cls,data): #!DELETE
        query="DELETE FROM joins WHERE user_id=%(user_id)s AND trip_id=%(trip_id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)

    #* ***********SELECT ONE JOINED TRIP***********
    @classmethod
    def one_joined_trip(cls,data): #!READ
        query="""SELECT * FROM trips
                JOIN joins ON trips.id = joins.trip_id
                JOIN users ON joins.user_id = users.id
                WHERE joins.trip_id=%(trip_id)s AND joins.user_id=%(user_id)s;
            """
        result= connectToMySQL(DATABASE).query_db(query,data)
        if len(result)<1:
            return False
        
        return result[0]

    #* ***********VALIDATE TRIP*********** 
    @staticmethod #!VALIDATION
    def validate_trip(data): 
        is_valid = True

        if len(data['destination'])<3:
            flash("Destination must be more than 3 characters!","trip")
            is_valid = False
        now = datetime.now()
        date_only = now.date()
        if data['start_date']<str(date_only):
            flash("Start Date must be in the future!","trip")
            is_valid = False
        if data['end_date']<data['start_date']:
            flash("End Date must be after the start date","trip")
            is_valid = False
        if data['end_date']=="":
            flash("End Date must be not blank!","trip")
            is_valid = False
        if len(data['plan'])<3:
            flash("Plan must be more than 3 characters!","trip")
            is_valid = False

            
        return is_valid
    


