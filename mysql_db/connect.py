import mysql.connector
from mysql_db.config import config

def connect_db():
    """ Connect to the MySQL database server """
    print("Inside connect db")
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the MySQL server
        print('Connecting to the MySQL database...')
        conn = mysql.connector.connect(**params)
        
        # create a cursor
        cur = conn.cursor()
        
        # execute a statement
        print('MySQL database version:')
        cur.execute('SELECT version()')

        # display the MySQL database server version
        db_version = cur.fetchone()
        print(db_version)
        
        #Closing cursor
        cur.close()

        return conn 
       
    except (Exception, mysql.DatabaseError) as error:
        print(error)
        if conn is not None:
            conn.close()
            print('Database connection closed.')
