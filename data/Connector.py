import psycopg2
from psycopg2 import sql

""" Class Connector
"""
class Connector():
    """ Constructeur de la class
    :param user username
    ;param host localhost
    :param mdp  password
    :param port 5432 
    :param db   database name
    """
    def __init__(self,user="postgres",host="localhost", mdp="postgres", port="5432", db="piratage"):
        self.user = user
        self.host = host
        self.mdp = mdp
        self.port = port
        self.db = db
        self.conn = None

    """ Permet la connection à la base de données
    """
    def connect(self):
        try: 
            self.conn = psycopg2.connect(user=self.user, password=self.mdp, host=self.host, port=self.port, database=self.db)
            cursor = self.conn.cursor()
            print("Connecting to db")
            return cursor
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
      
    """ Permet la déconnection de la base de données 
    """
    def disconnect(self):
        print ("Disconnection from data base ")
        self.conn.close()  