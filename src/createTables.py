import mysql.connector

mydb = mysql.connector.connect(
  host="172.20.0.4",
  user="python",
  password="python",
  database="python"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")