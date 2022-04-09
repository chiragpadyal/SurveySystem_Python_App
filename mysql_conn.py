
import mysql.connector

mydb = mysql.connector.connect(
	host="localhost",
	user="chiragsp",
	password="admin",
	database="survery_system",
	port=3306
)


# mydb = mysql.connector.connect(
# 	host="localhost",
# 	user="root",
# 	password="1346790",
# 	database="survery_system",
# 	port=3306
# )