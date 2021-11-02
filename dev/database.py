import copy
import mysql.connector


class ConnectDB:

    def __init__(self):
        # print("hello")
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Nikhil@123",
            database="LoginData"
        )

        # pointer
        my_cursor = mydb.cursor()

        # create Database
        my_cursor.execute("CREATE DATABASE IF NOT EXISTS test_db")

        # print all the database name
        # my_cursor.execute("SHOW DATABASES")

        # for db in my_cursor:
        #     print(db[0])

        # count no. of database
        # my_cursor.execute("SHOW DATABASES")

        # print('Total count of database := ' + str(len(my_cursor.fetchall())))

        my_cursor.execute("SHOW DATABASES")
        tuple_inside_list = my_cursor.fetchall()

        generator = (num for num in tuple_inside_list if num[0] == 'test_db')

        database_found = False
        for num in generator:
            database_found = True

        if database_found:
            print("Database found")
            # my_cursor.execute("SHOW DATABASES")
            try:
                my_cursor = mydb.cursor()
                my_cursor.execute("SHOW TABLES")
            except:
                my_cursor.execute("CREATE TABLE")


    # def prt(self):
    #     print("3")



