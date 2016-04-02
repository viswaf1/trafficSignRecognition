import cv2
import numpy as np

# Callback Function for Trackbar (but do not any work)
def nothing(*arg):
    pass

# Code here
def SimpleTrackbar(Image, WindowName):
    # Generate trackbar Window Name
    TrackbarName = WindowName + "Trackbar"

    # Make Window and Trackbar
    cv2.namedWindow(WindowName)
    cv2.createTrackbar(TrackbarName, WindowName, 0, 255, nothing)

    # Allocate destination image
    Threshold = np.zeros(Image.shape, np.uint8)

    # Loop for get trackbar pos and process it
