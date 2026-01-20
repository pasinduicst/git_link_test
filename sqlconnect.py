from optparse import Values
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",       
    user="root", 
    password="",   
    database="hdit_db1"
)
20

mycursor = mydb.cursor()

id = int(input("ENTER YOUR ID : "))
name = input("ENTER NAME: ")
email = input("ENTER EMAIL: ")
birthday = input("ENTER BIRTHDAY (YYYY-MM-DD): ")


sql = "INSERT INTO users02(ID, NAME, EMAIL, BIRTHDAY) VALUES (%s, %s, %s, %s)"
val = (id, name, email, birthday)

mycursor.execute(sql, val)
mydb.commit()

print("ADDED NEW RECORD")

mycursor.close()
mydb.close()