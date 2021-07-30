import cv2
import ntpath
import os

import numpy as np


def extract_frames_folder(path):
    myList_Adv = os.listdir(path)
    if '.DS_Store' in myList_Adv:
        myList_Adv.remove('.DS_Store')
    number=np.size(myList_Adv)
    print(number, type(myList_Adv))
    for i in range(0,number):
        print(i)


extract_frames_folder("/Users/macbookpro/Library/Mobile Documents/com~apple~CloudDocs/PycharmProjects/OpenCV/Commercial-detection /src/videos")