
"""using SQLlite"""

from tkinter import *
import sqlite3 ##sqlite library ##data base.
try:

    connection=sqlite3.connect('studentManagement.db') #filename.

except:
    print("Unable To Connect")

else:
    print("Database opened successfully.")
    ###Establishment of the connection.
    ##Table creation --> CREATE TABLE if Not exists( Column1 <datatype>, Column2 <datatype>, Column3 <datatype>, ...);
    ##To make a connection with python--> connection.execute(sql command)
    STUDENT_ID="student_id"
    TABLE_NAME="Student_Management_System"
    STUDENT_PHONE = "student_phone"
    STUDENT_COLLEGE = "student_college"
    STUDENT_NAME = "student_name"


    connection.execute("CREATE TABLE IF NOT EXISTS " + TABLE_NAME +
                     "("+
                        STUDENT_ID +" INTEGER PRIMARY KEY " +
                        " AUTOINCREMENT, " +
                        STUDENT_NAME+" TEXT, " +
                        STUDENT_COLLEGE+" TEXT, " +
                        STUDENT_PHONE+" INTEGER );")


    def EnterDetails(NAME, COLLEGE, PHONE):
        print("inside the table.")
        connection.execute("INSERT INTO " + TABLE_NAME + "(" +
                            STUDENT_NAME + ", " +
                            STUDENT_COLLEGE + ", " +
                            STUDENT_PHONE + " )" +
                            "VALUES (?,?,?,?);",
                           (NAME, COLLEGE, PHONE)
                           )
        connection.commit()

    def ViewDetails():
        print("About to display the values.")
        connection.execute(" SELECT * FROM " + TABLE_NAME + ";")


