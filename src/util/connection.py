import mysql.connector


def select_data(query):
    mydb = mysql.connector.connect(
        host='localhost',
        user='guilherme',
        passwd='3141',
        database='USER'
    )

    def getData():
        mycursor = mydb.cursor()
        mycursor.execute(query)
        result = mycursor.fetchall()
        return result

    return getData()


def insert_data(query):
    mydb = mysql.connector.connect(
        host="localhost",
        user='guilherme',
        passwd='3141',
        database="USER"
    )

    def getData():
        mycursor = mydb.cursor()
        mycursor.execute(query)
        mydb.commit()
        print(mycursor.rowcount, "inserted.")

    return getData()


def remove_data(query):
    mydb = mysql.connector.connect(
        host="localhost",
        user='guilherme',
        passwd='3141',
        database="USER"
    )

    def getData():
        mycursor = mydb.cursor()
        mycursor.execute(query)
        mydb.commit()
        print(mycursor.rowcount, "user deleted.")

    return getData()
