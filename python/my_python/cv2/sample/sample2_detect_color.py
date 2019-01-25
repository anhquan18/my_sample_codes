# Python program for Detection of a  
# specific color(blue here) using OpenCV with Python 
import cv2 
import numpy as np  
  
# Webcamera no 0 is used to capture the frames 
cap = cv2.VideoCapture(0)  

# Indentify the range of bgr color in hsv space
lower_red = np.array([-2,100,100])
upper_red = np.array([2,255,255])
lower_blue = np.array([110,100,100]) 
upper_blue = np.array([130,255,255]) 
lower_green = np.array([50, 100, 100])
upper_green = np.array([70, 255, 255])
  
# This drives the program into an infinite loop. 
while(1):        
    # Captures the live stream frame-by-frame 
    res, frame = cap.read() # res check whether the cam is capturing any frame or not ||||| frame is the image numpy 8 bit matrix
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
  
# This creates a mask of blue coloured  
# objects found in the frame. 
    mask = cv2.inRange(hsv, lower_red, upper_red) 
    #if mask.all():
    #    print 'REDDDDDDDDDDDD',"\n"
  
# The bitwise and of the frame and mask is done so  
# that only the blue coloured objects are highlighted  
# and stored in res 
    res = cv2.bitwise_and(frame,frame, mask= mask) 
    cv2.imshow('frame',frame) 
    cv2.imshow('mask',mask) 
    cv2.imshow('res',res) # result
  
# This displays the frame, mask  
# and res which we created in 3 separate windows. 
    k = cv2.waitKey(5) & 0xFF
    if k == 27:  # escape key
        break
  
# Destroys all of the HighGUI windows. 
cv2.destroyAllWindows() 
  
# release the captured frame 
cap.release()
