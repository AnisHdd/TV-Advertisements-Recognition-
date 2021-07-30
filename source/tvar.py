""" """
import cv2
import ntpath
import os
import numpy as np
from database_sql import database


class tvar(object):
    def __init__(self):
        self.db = database("127.0.0.1", "root", "", "TvAdsReco")


    def insert_advertisements(self,name,path,ff_descriptor,lf_descriptor,duration):
        """ add a new ads in channels"""
        self.db.mycursor.execute("INSERT INTO advertisements (name,path,ff_descriptor,lf_descriptor,duration) VALUES "
                                 "(%s, %s, %s, %s, %s) "
                                 ,(name,path,ff_descriptor,lf_descriptor,duration))
        self.db.commit()
        print(self.db.mycursor.rowcount, "record inserted.")


    def extract_frames_file(self,path_file):
        """ Extract the first and the last frame from a given ads path"""
        cap = cv2.VideoCapture(path_file)
        cap.set(1, cap.get(cv2.CAP_PROP_FRAME_COUNT) - 1)
        _, last_frame = cap.read()
        cap.set(1, 1)
        _, first_frame = cap.read()
        name = ntpath.basename(path_file)
        # cv2.imshow("as", first_frame)
        # while True:
        #     ch = 0xFF & cv2.waitKey(1)  # Wait for a second
        #     if ch == 27:
        #         break
        return  first_frame, last_frame, name

    def extract_frames_folder(self,path):
        myList_Adv = os.listdir(path)
        if '.DS_Store' in myList_Adv:
            myList_Adv.remove('.DS_Store')
        for id in range(0,np.size(myList_Adv)):
            first_frame, last_frame, name= self.extract_frames_file(path+"/"+str(myList_Adv[id]))
            #cv2.imwrite(str(name)+"_"+"first_frame.jpeg",first_frame)
            #cv2.imwrite(str(name)+"_"+"last_frame.jpeg",last_frame)
            # print(str(name)+"_"+"first_frame.jpeg",first_frame)

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
detecteur.extract_frames_folder('/Users/macbookpro/Library/Mobile Documents/com~apple~CloudDocs/PycharmProjects/OpenCV/Commercial-detection /src/videos')
# detecteur.db.mycursor.execute("SHOW TABLES")
# for x in detecteur.db.mycursor:
#     print(x)
