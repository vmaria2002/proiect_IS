import mysql

mydb = mysql.connector.connect(
  host="localhost",
  user="Maria",
  password="Maq@hr89!3",
  database="cv"
)


def connector():
    return mydb.cursor()