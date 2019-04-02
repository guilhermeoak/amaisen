import mysql.connector

USER = 'guilherme'
PASSWD = '3141'
HOST = 'localhost'
DB = 'USER'

mydb = mysql.connector.connect(
    host=HOST,
    user=USER,
    passwd=PASSWD,
    database=DB
)


def select_data(query):

    def get_data():
        my_cursor = mydb.cursor()
        my_cursor.execute(query)
        result = my_cursor.fetchall()
        return result

    return get_data()


def insert_data(query):
    
    def get_data():
        my_cursor = mydb.cursor()
        my_cursor.execute(query)
        mydb.commit()
        print(my_cursor.rowcount, "inserted.")

    return get_data()


def remove_data(query):
    

    def get_data():
        my_cursor = mydb.cursor()
        my_cursor.execute(query)
        mydb.commit()
        print(my_cursor.rowcount, "USER deleted.")

    return get_data()
