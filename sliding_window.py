# import the necessary packages
from helpers import pyramid
from helpers import sliding_window
import time
import cv2
from detect import detectObject

# loop over the image pyramid

def sliding_window_algorithm(image, winH, winW, confidence, windowStepSize, windowMovingSpeed):
    for resized in pyramid(image, scale=1.5):
        # loop over the sliding window for each layer of the pyramid
        for (x, y, window) in sliding_window(resized, windowStepSize, windowSize=(winW, winH)):
            # if the window does not meet our desired window size, ignore it
            if window.shape[0] != winH or window.shape[1] != winW:
                continue
            
            # THIS IS WHERE I PROCESS THE WINDOW, APPLYING A
            # MACHINE LEARNING CLASSIFIER TO CLASSIFY THE CONTENTS OF THE
            # WINDOW
            t_img = resized[y:y+winH,x:x+winW]# the image which has to be predicted

            # test_img = np.expand_dims(np.expand_dims(t_img,axis =0), axis=0) # expanding the dimensions of the image to meet the dimensions of the trained model
            result = detectObject(t_img, confidence)

            clone = resized.copy()
            
            if result:
                cv2.rectangle(clone, (x, y), (x + winW, y + winH), (255, 0, 0), 2)
            else: 
                cv2.rectangle(clone, (x, y), (x + winW, y + winH), (0, 255, 0), 2)
                
            cv2.imshow("Window", clone)
            cv2.waitKey(1)
            time.sleep(windowMovingSpeed)