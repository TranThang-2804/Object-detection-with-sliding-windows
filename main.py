# construct the argument parser and parse the arguments
import argparse
import cv2
from sliding_window import sliding_window_algorithm

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# load the image and define the window width and height
image = cv2.imread(args["image"])

# ALGORITHM TUNNING
# detection confidence acceptance
confidence = 0.75

# sliding window configuration
windowStepSize = 32
windowMovingSpeed = 0.00001
(winW, winH) = (256, 256)

sliding_window_algorithm(image, winW, winH, confidence, windowStepSize, windowMovingSpeed)

