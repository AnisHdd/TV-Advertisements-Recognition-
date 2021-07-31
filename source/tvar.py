""" """
import cv2
import ntpath
import os
import numpy as np
from database_sql import database
import pickle
import mysql.connector

from sys import getsizeof
import json


class tvar(object):
    def __init__(self):
        self.db = database("127.0.0.1", "root", "", "TvAdsReco")

    def insert_advertisement(self, name, path, ff_descriptor, lf_descriptor, duration,date):
        """ add a new ads in advertisements"""
        self.db.mycursor.execute("INSERT INTO advertisements (name,path,ff_descriptor,lf_descriptor,duration, "
                                 "date) VALUES "
                                 "(%s, %s, %s, %s, %s, %s) "
                                 , (name, path, ff_descriptor, lf_descriptor, duration))
        self.db.commit()
        print(self.db.mycursor.rowcount, "record inserted.")

    def extract_des_file(self, path_file):
        """ Extract the first and the last frame from a given ads path"""
        orb = cv2.ORB_create(nfeatures=100)
        name = ntpath.basename(path_file)
        cap = cv2.VideoCapture(path_file)
        cap.set(1, cap.get(cv2.CAP_PROP_FRAME_COUNT) - 1)
        _, lf = cap.read()
        lf = cv2.cvtColor(lf, cv2.COLOR_BGR2GRAY)
        _, lf_des = orb.detectAndCompute(lf, None)
        cap.set(1, 1)
        _, ff = cap.read()
        ff = cv2.cvtColor(ff, cv2.COLOR_BGR2GRAY)
        _, ff_des = orb.detectAndCompute(ff, None)
        # cv2.imshow("as", lf)
        # while True:
        #     ch = 0xFF & cv2.waitKey(1)  # Wait for a second
        #     if ch == 27:
        #         break
        return ff_des, lf_des, name


    def extract_des_folder(self, path):
        list_ads = os.listdir(path)
        if '.DS_Store' in list_ads:
            list_ads.remove('.DS_Store')
        for i in range(0, np.size(list_ads)):
            ff_des, lf_des, name = self.extract_des_file(path + "/" + str(list_ads[i]))
            """"ecrire dans la bdd"""
            # cv2.imwrite(str(name)+"_"+"ff.jpeg",ff)
            # cv2.imwrite(str(name)+"_"+"lf.jpeg",lf)
            print(name)


    def describe(self):
        """ entree: path vers le videos --- > remplir la base de donnee advertisements """
        self.db.mycursor.execute("SHOW TABLES")
        for x in self.db.mycursor:
            print(x)
        pass

    def recognize(self):
        """entree video --- > chercher dans la bdd avdertisement la publicite et remplir la table apparitions """
        pass


#
detecteur = tvar()
ff_des, lf_des, name = detecteur.extract_des_file('/Users/macbookpro/Library/Mobile '
                                        'Documents/com~apple~CloudDocs/PycharmProjects/OpenCV/Commercial-detection '
                                        '/src/videos/DjezzyOredoo2.mp4')


""" Json"""
#encoder
# x=json.dumps(ff_des.tolist())
#decoder
# y=json.loads(x)

# mydb = mysql.connector.connect(
#     host="127.0.0.1",
#     user="root",
#     password="",
#     database="TvAdsReco"
# )
# mycursor = mydb.cursor()
# sql = "INSERT INTO advertisements (name, path, ff_descriptor, lf_descriptor, duration) VALUES (%s, %s, %s, %s, %s)"
# val = ("mobilis", "path",  x, x, "curtime()")
# mycursor.execute(sql, val)
# mydb.commit()

# mycursor.execute("select ff_descriptor from advertisements where id=1")
# record = mycursor.fetchone()
# joined_string = "".join(record)
# y=json.loads(joined_string)
# print(y==ff_des)
