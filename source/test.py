import cv2

orb = cv2.ORB_create(nfeatures=100)
bf = cv2.BFMatcher(cv2.NORM_HAMMING)

# last_frame = cv2.imread("../frames/DjezzyOredoo.mp4_last_frame.jpeg")
# cap = cv2.VideoCapture("../videos/DjezzyOredoo.mp4")
cap = cv2.VideoCapture("../videos/lactofibre-rkm-1-fy-algzayr.mp4")
cap.set(1, cap.get(cv2.CAP_PROP_FRAME_COUNT) - 500)
_, last_frame = cap.read()
last_frame = cv2.cvtColor(last_frame, cv2.COLOR_BGR2GRAY)
_, des_last_frame = orb.detectAndCompute(last_frame, None)
cv2.imwrite("../frames/test_last_frame.jpeg",last_frame)

cap = cv2.VideoCapture("../videos/DjezzyOredoo.mp4")
print("count", cap.get(cv2.CAP_PROP_FRAME_COUNT), "FPS",cap.get(cv2.CAP_PROP_FPS), "duration",cap.get(cv2.CAP_PROP_FRAME_COUNT)/cap.get(cv2.CAP_PROP_FPS))
# while True:
#     _, current_frame = cap.read()
#     current_frame = cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY)
#     _, des_current_frame = orb.detectAndCompute(current_frame, None)
#     cv2.imshow('current_frame', current_frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#     matches = bf.knnMatch(des_current_frame, des_last_frame, k=2)
#     good = []
#     for m, n in matches:
#         if m.distance < 0.80 * n.distance:
#             good.append([m])
#     threshold = len(good) / len(des_last_frame)
#     if threshold > .80:
#         print("end found")

