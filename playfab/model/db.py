# build-in modules
from datetime import datetime
import os
# 3rd party modules
import psycopg2
import pymongo


class MongoDB:

    connection = None
    db = None

    def __init__(self):
        try:
            str = "mongodb+srv://{0}:{1}@cluster0.epurfcr.mongodb.net/{2}?retryWrites=true&w=majority"
            str = str.format(os.environ.get("MONGODB_USER"), os.environ.get("MONGODB_PASS"), os.environ.get("MONGODB_BASE"))
            print("Connecting to the MongoDB database...")
            self.connection = pymongo.MongoClient(
                "mongodb+srv://" + os.environ.get("MONGODB_USER") + ":" + os.environ.get("MONGODB_PASS") + "@cluster0.epurfcr.mongodb.net/" + os.environ.get("MONGODB_BASE") + "?retryWrites=true&w=majority"
            )
            self.db = self.connection.playfab
            print("The connection was successful.")
        except Exception as error:
            print("Connection to the MongoDB database failed due to: ", error)

    def __del__(self):
        if self.connection is not None:
            self.connection.close()
            print("The connection to the MongoDB database has been closed.")

    def insert(self):
        return self.db.users.insert_one({"id": 1, "email": "jarekpoczta@wp.pl", "email_update": datetime.now(), "pass": "Kodpin89!", "pass_update": datetime.now()})

    def select(self):
        return self.db.users.find_one({"email_update": {"$gt": datetime.now()}})
    

class PostgreSQL:
    connection = None
    cursor = None

    def __init__(self):
        try:
            print("Connecting to the PostgreSQL database...")
            self.connection = psycopg2.connect(
                host     = os.environ.get("POSTGRESQL_HOST"),
                database = os.environ.get("POSTGRESQL_BASE"),
                user     = os.environ.get("POSTGRESQL_USER"),
                password = os.environ.get("POSTGRESQL_PASS"),
                port     = os.environ.get("POSTGRESQL_PORT")
            )
            self.cursor = self.connection.cursor()
        except (Exception, psycopg2.DatabaseError) as error:
            print("Connection to the PostgreSQL database failed due to: ", error)

    def __del__(self):
        if self.connection is not None:
            self.connection.close()
            print("The connection to the PostgreSQL database has been closed.")


    def insert(self, query, values):
        self.cursor.execute(query, values)
        self.connection.commit()

    def select(self):
        query = "SELECT * FROM users"
        self.cursor.execute(query)
        return self.cursor.fetchall()
