import cv2
import numpy as np
from PIL import Image

def AddImageToCenter(frame, x, y, img):
    pilim = Image.fromarray(frame)
    pilim.paste(img, box=(int(x) - 32, int(y) - 32), mask=img)
    frame = np.array(pilim)
    return frame

def PointSearch(frame, templateImage, sensitivity):
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    grayImage = cv2.cvtColor(img_label, cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(grayFrame, grayImage, cv2.TM_CCOEFF_NORMED)
    threshold = sensitivity
    locate = np.where(res >= threshold)
    return locate

cap = cv2.VideoCapture(0)
label = "refPoint.jpg"
speedo = Image.open('fly64.png').convert('RGBA')
img_label = cv2.imread(label)
heightPoint, widthPoint, channels = img_label.shape
count = 1
color_red = (0, 0, 255)
down_points = (640, 480)
a, b = 200, 200
left_ang = ((down_points[0] - a) // 2, (down_points[1] - b) // 2)
right_ang = ((down_points[0] - a) // 2 + a, (down_points[1] - b) // 2 + b)

while True:
    ret, frame = cap.read()
    loc = PointSearch(frame, img_label, 0.6)
    cv2.rectangle(frame, left_ang, right_ang, color_red, thickness=2, lineType=8, shift=0)  #
    if len(loc[0]) > 0:
        x = loc[1][0]
        y = loc[0][0]

        cv2.rectangle(frame, (x, y), (x + widthPoint, y + heightPoint), (0, 255, 0), 2)
        cx = x + widthPoint / 2
        cy = y + heightPoint / 2
        count +=1
        if cx >= 220 and cy >= 140 and x + widthPoint <= 440 and y + heightPoint <= 340:
            print(True)
        else:
            print(False)

        frame = AddImageToCenter(frame, cx,cy, speedo)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
