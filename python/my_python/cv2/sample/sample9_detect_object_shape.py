import cv2

def nothing(x):
    pass

cam = cv2.VideoCapture(0)

cv2.namedWindow('Edge Detection')
cv2.createTrackbar('T1', 'Edge Detection', 0, 600, nothing)
cv2.createTrackbar('T2', 'Edge Detection', 0, 600, nothing)

while True:
    ret, img = cam.read()
    threshold1 = cv2.getTrackbarPos('T1', 'Edge Detection')
    threshold2 = cv2.getTrackbarPos('T2', 'Edge Detection')

    # Bilateral Fileter help even out the image surface. preserving the edge
    filtered_img = cv2.bilateralFilter(img, 5, threshold1, threshold2)
    edge_img = cv2.Canny(filtered_img, 100, 200) # lower thresshold and upper threshold

    cv2.imshow("Edge Detection", edge_img)
    cv2.waitKey(5)
