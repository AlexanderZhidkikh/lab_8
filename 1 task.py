import cv2


ImgBgr = cv2.imread('variant-3.jpeg')

ImgHsv = cv2.cvtColor(ImgBgr, cv2.COLOR_BGR2HSV)
cv2.imwrite('hsv_image.jpeg', ImgHsv)

cv2.imshow("BGR", ImgBgr)
cv2.imshow('HSV', ImgHsv)



cv2.waitKey(0)