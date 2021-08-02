from typing import Tuple

import cv2
import ntpath
import os
import numpy as np
from database_sql import database
from sys import getsizeof
import json
import time
from datetime import datetime


class TAR(object):
    def __init__(self):
        self.db = database("127.0.0.1", "root", "", "TvAdsReco")
        self.conn = self.db.connect()

    def Json_encode(self, numpy1, numpy2):

        return json.dumps(numpy1.tolist()), json.dumps(numpy2.tolist())

    # def Json_decode(json_bdd):
    # 
    #     return json.loads("".join(json_bdd))

    @staticmethod
    def frames_hash(frame1, frame2, hashSize=8):
        """image should be black and white"""
        frame1 = cv2.resize(frame1, (426, 240))    #Todo rajouter une fonction qui convertit tous les fichiers en mp4 et resize en (426, 240).
        resized1 = cv2.resize(frame1, (hashSize + 1, hashSize))
        diff1 = resized1[:, 1:] > resized1[:, :-1]
        frame2 = cv2.resize(frame2, (426, 240))    #Todo rajouter une fonction qui convertit tous les fichiers en mp4 et resize en (426, 240).
        resized2 = cv2.resize(frame2, (hashSize + 1, hashSize))
        diff2 = resized2[:, 1:] > resized2[:, :-1]
        return sum([2 ** i for (i, v) in enumerate(diff1.flatten()) if v]), sum([2 ** i for (i, v) in enumerate(diff2.flatten()) if v])

    @staticmethod
    def get_frames(cap):
        cap.set(1, 1)
        _, first_frame = cap.read()
        cap.set(1, cap.get(cv2.CAP_PROP_FRAME_COUNT) - 1)
        _, last_frame = cap.read()
        # first_frame = cv2.resize(first_frame, (426, 240))
        return cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY), cv2.cvtColor(last_frame, cv2.COLOR_BGR2GRAY)
    #
    # def get_last_frame(self, cap):
    #
    #     # last_frame = cv2.resize(last_frame, (426, 240))
    #     return cv2.cvtColor(last_frame, cv2.COLOR_BGR2GRAY)

    def extract_des_file(self, path_file):
        """ Extract the descriptors of the first and the last frame from a given ads path"""
        """last frame"""
        orb = cv2.ORB_create(nfeatures=100)
        cap = cv2.VideoCapture(path_file)
        first_frame, last_frame = self.get_frames(cap)
        """ Wrinting the frames in frames directory """
        # ads = os.path.basename(path_file)
        # cv2.imwrite("/Users/macbookpro/PycharmProjects/TV-Advertisements-Recognition-/frames/"+ads+"_"+"first_frame.jpeg", first_frame)
        # cv2.imwrite("/Users/macbookpro/PycharmProjects/TV-Advertisements-Recognition-/frames/"+ads+"_"+"last_frame.jpeg", last_frame)
        first_frame_hash, last_frame_hash = self.frames_hash(first_frame, last_frame)
        _, des_last_frame = orb.detectAndCompute(last_frame, None)
        _, des_first_frame = orb.detectAndCompute(first_frame, None)
        hash_file = np.int(str(first_frame_hash) + str(last_frame_hash))
        duration = (cap.get(cv2.CAP_PROP_FRAME_COUNT)) / cap.get(cv2.CAP_PROP_FPS)
        # cv2.imshow("as", first_frame)
        # while True:
        #     ch = 0xFF & cv2.waitKey(1)  # Wait for a second
        #     if ch == 27:
        #         break
        return des_first_frame, des_last_frame, duration, hash_file

    def extract_des_folder(self, path):
        start = time.time()
        list_ads = os.listdir(path)
        if '.DS_Store' in list_ads:
            list_ads.remove('.DS_Store')
        for ads in list_ads:
            des_first_frame, des_last_frame, duration, hash_file = self.extract_des_file(
                path + "/" + ads)
            if self.db.check_duplicate(hash_file):
                print("the hash of {} already exists".format(ads))
            else:
                des_first_frame, des_last_frame = self.Json_encode(des_first_frame, des_last_frame)
                self.db.insert_advertisement(ads, path + "/" + ads, des_first_frame, des_last_frame,
                                             duration, hash_file)
                print("The advertisement {} was added {} seconds".format(ads,time.time()- start))

        print("All advertisements have been added in {} seconds".format(time.time()- start))

    def recognize(self):
        """entree video --- > chercher dans la bdd avdertisement la publicite et remplir la table apparitions """
        pass


#
detecteur = TAR()
detecteur.extract_des_folder("/Users/macbookpro/PycharmProjects/TV-Advertisements-Recognition-/videos")
# if detecteur.db.check_duplicate(6026277995680978239868082074056418304):
#     print("hash already exists")
# else :
#     print("insert ......")
# print (resultat, type(resultat))
# # detecteur.db.insert_channel("adel", "ééééé")

# print(type(desc_f))

# json_str = json.dumps(x.tolist())
# print(print(json_str),type(json_str) ,getsizeof(json_str))
# x = np.array(json_str)
# x.reshape(100)
# print(print(x),type(x) ,getsizeof(x),np.size(x))

# detecteur.db.mycursor.execute("SHOW TABLES")
# for x in detecteur.db.mycursor:
#     print(x)
