""" """
import cv2
import ntpath
import os
import numpy as np
from database_sql import database
from sys import getsizeof
import json


class tvar(object):
    def __init__(self):
        self.db = database("127.0.0.1", "root", "", "TvAdsReco")

    def insert_advertisement(self, name, path, ff_descriptor, lf_descriptor, duration):
        """ add a new ads in advertisement"""
        self.db.mycursor.execute("INSERT INTO advertisements (name,path,ff_descriptor,lf_descriptor,duration) VALUES "
                                 "(%s, %s, %s, %s, %s) "
                                 , (name, path, ff_descriptor, lf_descriptor, duration))
        self.db.commit()
        print(self.db.mycursor.rowcount, "record inserted.")
    
    def insert_channel(self, name, url):
            """ add a new channel in channels"""
        self.db.mycursor.execute("INSERT INTO channels (name,url) VALUES "
                                 "(%s, %s) "
                                 , (name, url))
        self.db.commit()
        pass
    
    def insert_brand(self, name):
            """ add a new brand in brands"""
        self.db.mycursor.execute("INSERT INTO channels (name) VALUES "
                                 "(%s) "
                                 , (name))
        self.db.commit()
        pass

    def insert_apparition(self, id_advetisements,id_channel,time_start,time_end):
            """ add a new apparition in apparitions"""
        self.db.mycursor.execute("INSERT INTO channels (id_advetisements,id_channel,time_start,time_end) VALUES "
                                 "(%s,%s,%s,%s) "
                                 , (id_advetisements,id_channel,time_start,time_end))
        self.db.commit()
        pass


    def extract_frames_file(self, path_file):
        """ Extract the first and the last frame from a given ads path"""
        orb = cv2.ORB_create(nfeatures=100)
        name = ntpath.basename(path_file)
        cap = cv2.VideoCapture(path_file)
        cap.set(1, cap.get(cv2.CAP_PROP_FRAME_COUNT) - 1)
        _, last_frame = cap.read()
        last_frame = cv2.cvtColor(last_frame, cv2.COLOR_BGR2GRAY)
        _, des_last_frame = orb.detectAndCompute(last_frame, None)
        cap.set(1, 1)
        _, first_frame = cap.read()
        first_frame = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)
        _, des_first_frame = orb.detectAndCompute(first_frame, None)
        # cv2.imshow("as", last_frame)
        # while True:
        #     ch = 0xFF & cv2.waitKey(1)  # Wait for a second
        #     if ch == 27:
        #         break
        return des_first_frame, des_last_frame, name

    def extract_frames_folder(self, path):
        list_ads = os.listdir(path)
        if '.DS_Store' in list_ads:
            list_ads.remove('.DS_Store')
        for i in range(0, np.size(list_ads)):
            des_first_frame, des_last_frame, name = self.extract_frames_file(path + "/" + str(list_ads[i]))
            # cv2.imwrite(str(name)+"_"+"first_frame.jpeg",first_frame)
            # cv2.imwrite(str(name)+"_"+"last_frame.jpeg",last_frame)
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
detecteur.extract_frames_folder('/Users/macbookpro/Library/Mobile '
                                        'Documents/com~apple~CloudDocs/PycharmProjects/OpenCV/Commercial-detection '
                                        '/src/videos')


# json_str = json.dumps(x.tolist())
# print(print(json_str),type(json_str) ,getsizeof(json_str))
# x = np.array(json_str)
# x.reshape(100)
# print(print(x),type(x) ,getsizeof(x),np.size(x))

# detecteur.db.mycursor.execute("SHOW TABLES")
# for x in detecteur.db.mycursor:
#     print(x)
