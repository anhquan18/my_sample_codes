# import the necessary packages
import argparse
import cv2


cap = cv2.VideoCapture(0)
 
# construct the argument parser and parse the arguments
#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", required = True,
#	help = "Path to the image to be thresholded")
#ap.add_argument("-t", "--threshold", type = int, default = 128,
#	help = "Threshold value")
#args = vars(ap.parse_args())
 
# load the image and convert it to grayscale
ret, image = cap.read()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = 127
 
# initialize the list of threshold methods
methods = [
	("THRESH_BINARY", cv2.THRESH_BINARY),         # Pixel with gray scale value bigger than threshold will be white 255, smaller will be black 0
	("THRESH_BINARY_INV", cv2.THRESH_BINARY_INV), # p's value bigger than threshold will be black, smaller will be white
	("THRESH_TRUNC", cv2.THRESH_TRUNC),           # p's value smaller than threshold will remain the same, bigger will be black
	("THRESH_TOZERO", cv2.THRESH_TOZERO),         # p's value bigger than threshold remain the same, sammler will be black
	("THRESH_TOZERO_INV", cv2.THRESH_TOZERO_INV)] # p's value bigger than threshold will be black, smaller remain the same
 
# loop over the threshold methods
while thresh != 0:
    cv2.imshow('Picture', image)
    for (threshName, threshMethod) in methods:
            # threshold the image and show it
            #(T, thresh) = cv2.threshold(gray, ["threshold"], 255, threshMethod)
            print(threshName, threshMethod)
            (T, threshold_image) = cv2.threshold(gray, thresh, 255, threshMethod)
            cv2.imshow(threshName, threshold_image)
            cv2.waitKey(0)
    cv2.destroyAllWindows()
    thresh = int(input('Input thresh: '))
