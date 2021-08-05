#!/usr/bin/python

from sqlalchemy import create_engine
from os import environ
from sys import stderr,stdout




DWS_MYSQL_DATABASE_URI = environ.get('DWS_MYSQL_DATABASE_URI','None' )


# ~ Host: sql4.freesqldatabase.com
# ~ Database name: sql4429170
# ~ Database user: sql4429170
# ~ Database password: tTMQBS7EVl
# ~ Port number: 3306
# ~ root:pass@localhost/mydb"



def check_db_connection():
    
    try:
        connection = create_engine('mysql+pymysql://' + DWS_MYSQL_DATABASE_URI)
        db = connection.connect()
        
        
          
    except:
        print("Error while connecting to MySQL Server", file = stderr)
        return 1
     
     
    print("conneted successfully to MySql Database")   
    return 0 



if __name__ == '__main__' :
    connection_status = check_db_connection()
    print(connection_status)
