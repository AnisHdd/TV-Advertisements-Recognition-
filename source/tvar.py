import cv2
import ntpath
import os
import numpy as np
from database_sql import database
from sys import getsizeof
import json
from datetime import datetime


class tvar(object):
    def __init__(self):
        self.db = database("127.0.0.1", "root", "", "TvAdsReco")
        self.conn = self.db.connect()

    def Json_encode(self, numpy):

        return json.dumps(numpy.tolist())

    def Json_decode(json_bdd):

        return json.loads("".join(json_bdd))

    def extract_frames_file(self, path_file):
        """ Extract the first and the last frame from a given ads path"""
        orb = cv2.ORB_create(nfeatures=100)
        # name = ntpath.basename(path_file)
        cap = cv2.VideoCapture(path_file)
        cap.set(1, cap.get(cv2.CAP_PROP_FRAME_COUNT) - 1)
        _, last_frame = cap.read()
        last_frame = cv2.cvtColor(last_frame, cv2.COLOR_BGR2GRAY)
        _, des_last_frame = orb.detectAndCompute(last_frame, None)
        cap.set(1, 1)
        _, first_frame = cap.read()
        first_frame = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)
        _, des_first_frame = orb.detectAndCompute(first_frame, None)
        # duration = cap.get(cv2.CAP_PROP_POS_MSEC)
        duration = (cap.get(cv2.CAP_PROP_FRAME_COUNT)) / cap.get(cv2.CAP_PROP_FPS)
        # cv2.imshow("as", last_frame)
        # while True:
        #     ch = 0xFF & cv2.waitKey(1)  # Wait for a second
        #     if ch == 27:
        #         break
        return des_first_frame, des_last_frame, duration

    def extract_frames_folder(self, path):
        list_ads = os.listdir(path)
        if '.DS_Store' in list_ads:
            list_ads.remove('.DS_Store')
        for i in range(0, np.size(list_ads)):
            des_first_frame, des_last_frame, duration = self.extract_frames_file(path + "/" + str(list_ads[i]))
            # print(path + "/" + str(list_ads[i]))
            des_first_frame = self.Json_encode(des_first_frame)
            des_last_frame = self.Json_encode(des_last_frame)
            self.db.insert_advertisement(list_ads[i], path + "/" + str(list_ads[i]), des_first_frame, des_last_frame,
                                         duration)
            # print(type(des_first_frame),type(des_last_frame));
            # cv2.imwrite(str(name)+"_"+"first_frame.jpeg",first_frame)
            # cv2.imwrite(str(name)+"_"+"last_frame.jpeg",last_frame)
            # print()

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
detecteur.extract_frames_folder("/Users/macbookpro/Library/Mobile Documents/com~apple~CloudDocs/PycharmProjects/OpenCV/Commercial-detection /src/videos")
# detecteur.db.insert_channel("adel", "ééééé")

# print(type(desc_f))

# json_str = json.dumps(x.tolist())
# print(print(json_str),type(json_str) ,getsizeof(json_str))
# x = np.array(json_str)
# x.reshape(100)
# print(print(x),type(x) ,getsizeof(x),np.size(x))

# detecteur.db.mycursor.execute("SHOW TABLES")
# for x in detecteur.db.mycursor:
#     print(x)
