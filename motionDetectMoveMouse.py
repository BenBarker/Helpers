'''Move the mouse based on input from webcam. If motion is detected the mouse is moved.
This is to switch scenes in OBS (screen recording and streaming software) based on camera activity.
OBS supports automatic switching based on mouse activity, but not camera activity. This hacks around that.

Requires opencv-python, imutils, pyautogui, and numpy, and "Advanced Scene Switcher" for OBS.
Script should be started then Advanced Scene Switcher configured to switch scenes based on idle detection.
I apologize in advance for how hacky this is.
'''
import cv2
import imutils
import time
import pyautogui

#set up video capture
cv2.namedWindow("preview")
vc = cv2.VideoCapture(2) #change this number for your video capture device number.

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

firstFrame = None
alternate = False

#Begin motion detection.
#This basic motion detection requires only modest input, so the image is read infrequently,
#at a low resolution, and blurred and thresholded. The goal is to reduce CPU demands.
while rval:
    time.sleep(0.1) #delay between frames. 
    rval, frame = vc.read()
    frame = imutils.resize(frame,width=128) #Resize image very small
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #convert to greyscale
    gray = cv2.GaussianBlur(gray, (9,9),0) #blur image

    if firstFrame is None:
        firstFrame = gray
        continue

    #threshold and find contours. If contours have significant area then motion is detected.
    frameDelta = cv2.absdiff(firstFrame,gray)
    thresh = cv2.threshold(frameDelta, 25,255,cv2.THRESH_BINARY)[1]
    thresh = cv2.dilate(thresh, None, iterations=2)

    #this function may return (cnts, _) on older versions of cv2. If you get an exception try that.
    (_, cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    # loop over the contours
    for c in cnts:
        # if the contour is too small, ignore it
        if cv2.contourArea(c) < 500:
            continue
        else:
            #motion detected, jiggle mouse one pixel
            moveAmt = 1
            if not alternate:
                moveAmt *= -1
            alternate = not alternate
            pyautogui.moveRel(None,moveAmt)

    #uncomment to show window. Not required to move mouses
    #cv2.imshow("preview", thresh)

    #exit on ESC
    key = cv2.waitKey(20)
    if key == 27: 
        break
cv2.destroyWindow("preview")


