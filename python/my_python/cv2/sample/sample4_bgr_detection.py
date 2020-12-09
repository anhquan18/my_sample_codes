import cv2

cap = cv2.VideoCapture(0)

red_thresh = 220
green_thresh = 150
blue_thresh = 220
escape = 27

while(1):
    res, frame = cap.read()

    height, width, depth = frame.shape

    mid_h, mid_w = int(height/2), int(width/2)
    blue, green, red = frame[mid_h, mid_w]

    if red >= red_thresh: print "RED"
    if green >= green_thresh: print "GREEN"
    if blue >= blue_thresh: print "BLUE"

    cv2.imshow("FRAME", frame)

    key = cv2.waitKey(5)
    if key == escape:
        break

cv2.destroyAllWindows()
cap.release()
