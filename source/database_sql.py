import mysql.connector


""" Create  mysql database "TvAdsReco" """
""" Connecte to the database "TvAdsReco" """
mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Plop123",
    database="TvAdsReco"
)
mycursor = mydb.cursor()

"""
Create the table "advertisements" 
Ex : [id*(int20), id_brand(int20), name(VARCHAR(225)), path(VARCHAR(225)) ,ffdes(json), lfdes(json), duration(time), date(timestamp)]
    =[1, 1, mobilis1,...,...,...,...]
     [2, 1, mobilis2,...,...,...,...] 
"""
mycursor.execute("CREATE TABLE IF NOT EXISTS advertisements(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), "
                 "path VARCHAR(255), ff_descriptor JSON, lf_descriptor JSON, duration TIME, created_at TIMESTAMP "
                 "DEFAULT CURRENT_TIMESTAMP)")

""""
Create the table brands 
Ex : [id, name, created_at] = [1 mobilis] 
"""
mycursor.execute("CREATE TABLE IF NOT EXISTS brands(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), created_at "
                 "TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")

""""
Create the table channels 
Ex : [id, name, url] 
"""
mycursor.execute("CREATE TABLE IF NOT EXISTS channels(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), "
                 "url VARCHAR(255))")

""""
Create the table apparitions 
Ex : [id, id_advetisements, id_channel, time_start, time_end, date]
"""
mycursor.execute("CREATE TABLE IF NOT EXISTS apparitions(id INT AUTO_INCREMENT PRIMARY KEY, id_advetisements INT, "
                 "id_channel INT, time_start TIME, time_end TIME, appeared_at TIMESTAMP)")


class database(object):
    def __init__(self, host, user, password, database_name):
        self.host = host
        self.user = user
        self.password = password
        self.database_name = database_name


    def connect(self):
        self.mydb = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database_name
        )
        self.mycursor = self.mydb.cursor()
        return self.mydb;
    
    def insert_advertisement(self, name, path, ff_descriptor, lf_descriptor, duration):
        """ add a new ads in advertisement"""
        self.mycursor.execute("INSERT INTO advertisements (name,path,ff_descriptor,lf_descriptor,duration) VALUES (%s, %s, %s, %s, %s) " , (name, path, ff_descriptor, lf_descriptor, duration))
        self.mydb.commit()

    def insert_channel(self, name, url):
        """ add a new channel in channels"""
        self.mycursor.execute("INSERT INTO channels (name,url) VALUES (%s, %s) ", (name, url))
        self.mydb.commit()

    def insert_brand(self, name):
        """ add a new brand in brands"""
        self.mycursor.execute("INSERT INTO channels (name) VALUES "
                                 "(%s) "
                                 , (name))
        self.mydb.commit()

    def insert_apparition(self, id_advetisements,id_channel,time_start,time_end):
        """ add a new apparition in apparitions"""
        self.mycursor.execute("INSERT INTO channels (id_advetisements,id_channel,time_start,time_end) VALUES "
                                 "(%s,%s,%s,%s) "
                                 , (id_advetisements,id_channel,time_start,time_end))
        self.mydb.commit()
        


#####
# db = database("127.0.0.1", "root", "", "TvAdsReco")
# db.mycursor.execute("SHOW TABLES")
# for x in db.mycursor:
#   print(x)
# Ex : [id, name, url]
# mycursor = mydb.cursor()
# sql = "INSERT INTO channels (name, url) VALUES (%s, %s)"
# val = ("elbilad", "https://www.nikemok.zebi")
# mydb.commit()
# print(mycursor.rowcount, "record inserted.")