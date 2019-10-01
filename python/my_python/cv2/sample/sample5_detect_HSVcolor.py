import numpy as np
import cv2 

x_cor, y_cor = 0, 0

def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global x_cor, y_cor
        print("mouse clicked")
        x_cor, y_cor = x, y
        print("x, y value:", x_cor, y_cor)
    print("event:", event)
    print("x, y =", x, y)
    print("flags:", flags)
    print("param:", param)
    print("\n")

cap = cv2.VideoCapture(0)
frame = []
cv2.namedWindow('frame')
cv2.setMouseCallback('frame', mouse_callback, frame)


object_BGRcolor = np.array([0,0,0])

while(1):
    _, frame = cap.read()

    cv2.imshow('frame', frame)

    k = cv2.waitKey(5) & 0xFF
    if k == 27: #Escape key
        break

    if k == ord('a'):
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_object_color = hsv[x_cor][y_cor][0] - 10, 100, 100
        upper_object_color = hsv[x_cor][y_cor][0] + 10, 255, 255
        print("lower_color:", lower_object_color)
        print("upper_color:", upper_object_color)

cv2.destroyAllWindows()
cv2.cap.release()
