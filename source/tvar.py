import cv2
import ntpath
import os
import numpy as np
from database_sql import database
from sys import getsizeof
import json
from datetime import datetime


class TAR(object):
    def __init__(self):
        self.db = database("127.0.0.1", "root", "", "TvAdsReco")
        self.conn = self.db.connect()

    def Json_encode(self, numpy):

        return json.dumps(numpy.tolist())

    def Json_decode(json_bdd):

        return json.loads("".join(json_bdd))

    def frame_hash(self, frame, hashSize=8):
        """image should be black and white"""
        frame= cv2.resize(frame, (426, 240))    #Todo rajouter une fonction qui convertit tous les fichiers en mp4 et resize en (426, 240).
        resized = cv2.resize(frame, (hashSize + 1, hashSize))
        diff = resized[:, 1:] > resized[:, :-1]
        return sum([2 ** i for (i, v) in enumerate(diff.flatten()) if v])

    def get_first_frame(self, cap) -> object:
        cap.set(1, 1)
        _, first_frame = cap.read()
        # first_frame = cv2.resize(first_frame, (426, 240))
        return cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)

    def get_last_frame(self, cap):
        cap.set(1, cap.get(cv2.CAP_PROP_FRAME_COUNT) - 1)
        _, last_frame = cap.read()
        # last_frame = cv2.resize(last_frame, (426, 240))
        return cv2.cvtColor(last_frame, cv2.COLOR_BGR2GRAY)

    def extract_frames_file(self, path_file):
        """ Extract the first and the last frame from a given ads path"""
        """last frame"""
        orb = cv2.ORB_create(nfeatures=100)
        cap = cv2.VideoCapture(path_file)
        # cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        # cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)

        last_frame = self.get_last_frame(cap)

        last_frame_hash = self.frame_hash(last_frame)
        _, des_last_frame = orb.detectAndCompute(last_frame, None)
        """first frame"""
        first_frame = self.get_first_frame(cap)
        first_frame_hash = self.frame_hash(first_frame)
        _, des_first_frame = orb.detectAndCompute(first_frame, None)
        """ ads hash"""
        hash_file = np.int(str(first_frame_hash) + str(last_frame_hash))
        """duration"""
        duration = (cap.get(cv2.CAP_PROP_FRAME_COUNT)) / cap.get(cv2.CAP_PROP_FPS)
        # cv2.imshow("as", first_frame)
        # while True:
        #     ch = 0xFF & cv2.waitKey(1)  # Wait for a second
        #     if ch == 27:
        #         break
        return des_first_frame, des_last_frame, duration, hash_file

    def extract_frames_folder(self, path):
        list_ads = os.listdir(path)
        if '.DS_Store' in list_ads:
            list_ads.remove('.DS_Store')
        for i in range(0, np.size(list_ads)):
            des_first_frame, des_last_frame, duration, hash_file = self.extract_frames_file(
                path + "/" + str(list_ads[i]))
            print(hash_file)
            if self.db.check_duplicate(hash_file):
                print("the hash of {} already exists".format(str(list_ads[i])))
            else:
                # print(path + "/" + str(list_ads[i]))
                des_first_frame = self.Json_encode(des_first_frame)
                des_last_frame = self.Json_encode(des_last_frame)
                self.db.insert_advertisement(list_ads[i], path + "/" + str(list_ads[i]), des_first_frame, des_last_frame,
                                             duration, hash_file)
            # print(type(des_first_frame),type(des_last_frame));
            # cv2.imwrite(str(list_ads[i])+"_"+"first_frame.jpeg",first_frame)
            # cv2.imwrite(str(list_ads[i])+"_"+"last_frame.jpeg",last_frame)
            # print()

    def recognize(self):
        """entree video --- > chercher dans la bdd avdertisement la publicite et remplir la table apparitions """
        pass


#
detecteur = TAR()
detecteur.extract_frames_folder("/Users/macbookpro/PycharmProjects/TV-Advertisements-Recognition-/videos")
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
