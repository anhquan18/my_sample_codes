#!/usr/bin/env python3.6

from __future__ import print_function
import cv2
from ar_markers import detect_markers


if __name__ == "__main__":
    print('Press "q" to quit')
    camera0 = cv2.VideoCapture(0)

    if camera0.isOpened(): #try to get the first frame
        frame_captured, frame = camera0.read()
    else:
        frame_captured = False

    while frame_captured:
        gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #markers = detect_markers(frame)
        markers = detect_markers(gray_scale)
        print("markers:\n", markers)
        for marker in markers:
            marker.highlite_marker(gray_scale)
        cv2.imshow('Test Frame', gray_scale)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        frame_captured, frame = camera0.read()

    #When everything done, release the camera0
    camera0.release()
    cv2.destroyAllWindows()

