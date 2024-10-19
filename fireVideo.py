# Importing all necessary libraries
import cv2
import os
import time

# Read the video from specified path
cam = cv2.VideoCapture("./videos/coffeePotFire.mp4")

currentframe = 0

while (True):
    time.sleep(5) # take schreenshot every 5 seconds
    # reading from frame
    ret, frame = cam.read()

    if ret:
        # if video is still left continue creating images
        name = './data/coffeePotFire/frame' + str(currentframe) + '.jpg'
        print('Creating...' + name)

        # writing the extracted images
        cv2.imwrite(name, frame)

        # increasing counter so that it will
        # show how many frames are created
        currentframe += 1
    else:
        break

# Release all space and windows once done
cam.release()
cv2.destroyAllWindows()
