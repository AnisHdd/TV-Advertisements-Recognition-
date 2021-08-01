import cv2
img = cv2.imread("/Users/macbookpro/Library/Mobile Documents/com~apple~CloudDocs/PycharmProjects/OpenCV/Commercial-detection /src/Adv/oredoo0/End.jpg")
img2= cv2.resize(img,(426, 240))
print(img.shape, img2.shape)
cv2.imshow("as", img)
while True:
    ch = 0xFF & cv2.waitKey(1)  # Wait for a second
    if ch == 27:
        break