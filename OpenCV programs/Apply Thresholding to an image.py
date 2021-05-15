import cv2
img = cv2.imread("tiger.jpg")
grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
thresImg = cv2.threshold(grayImg,80,255,cv2.THRESH_BINARY)[1]
cv2.imwrite("thresholdImage2.jpg",thresImg)
