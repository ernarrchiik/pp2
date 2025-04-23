import psycopg2
from config import load_config

def connect(config):
    """ Connect to the PostgreSQL database server """
    
    try:
        # connecting to the PostgreSQL server
        with psycopg2.connect(**config) as conn:
            print('Connected to the PostreSQL server') 
            return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

config = load_config()
connect(config)