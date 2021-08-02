import cv2

orb = cv2.ORB_create(nfeatures=100)
bf = cv2.BFMatcher(cv2.NORM_HAMMING2)
img=cv2.imread("/Users/macbookpro/PycharmProjects/TV-Advertisements-Recognition-/frames/Dima Ooredoo خير بدل جدد.mp4_first_frame.jpeg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, des1 = orb.detectAndCompute(img, None)
print(type(des1))
