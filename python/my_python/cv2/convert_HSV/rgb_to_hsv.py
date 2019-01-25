import sys
import numpy as np
import cv2

#rgb
red = sys.argv[1]
green = sys.argv[2]
blue = sys.argv[3]

color = np.uint8([[[blue, green, red]]])
hsv = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)

print "hsv: ", hsv

hue = hsv[0][0][0]

print("Lower bound is: "), 
print("[" + str(hue - 10) + ", 100, 100]\n")

print("Upper bound is: "),
print("[" + str(hue + 10) + ", 255, 255]")
