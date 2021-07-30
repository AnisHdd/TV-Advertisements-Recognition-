import mysql.connector
""" Create  mysql database "TvAdsReco" """
# mydb = mysql.connector.connect(
#     host="127.0.0.1",
#     user="root",
#     password=""
# )
# mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE TvAdsReco")
# mycursor.execute("SHOW DATABASES")
#
# for x in mycursor:
#   print(x)
""" Connecte to the database "TvAdsReco" """
mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="TvAdsReco"
)
mycursor = mydb.cursor()

"""Create the table "advertisements" """
mycursor.execute("CREATE TABLE IF NOT EXISTS advertisements(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), path VARCHAR(255))")
mycursor.execute("CREATE TABLE IF NOT EXISTS descriptors(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), first_frame VARCHAR(255),last_frame VARCHAR(255) )")


""" Create an auto incremeant colonne for each table"""
#mycursor.execute("ALTER TABLE advertisements ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
#mycursor.execute("ALTER TABLE descriptors ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
#mycursor.execute("ALTER TABLE apparitions ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

"""Create columns of the table advertisements  """
mycursor.execute("SHOW TABLES")
for x in mycursor:
  print(x)