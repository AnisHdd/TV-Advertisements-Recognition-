import argparse
import numpy as np
import time
import sys
import cv2
import os


def frame_hash(image, hashSize=8):
    """image should be black and white"""
    resized = cv2.resize(image, (hashSize + 1, hashSize))
    diff = resized[:, 1:] > resized[:, :-1]
    return sum([2 ** i for (i, v) in enumerate(diff.flatten()) if v])

image = cv2.imread("/Users/macbookpro/Library/Mobile Documents/com~apple~CloudDocs/PycharmProjects/OpenCV/Commercial-detection /src/test.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

hash1  = frame_hash(image)
hash2  = frame_hash(image)
hash3  = str(hash1) + str(hash2)
hash3  = np.int(str(hash1) + str(hash2))
print(hash1, hash2, hash3, type(hash3))