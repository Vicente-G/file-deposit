import cv2 as cv
import os
import sys
import shutil

COUNTER = 1
FOLDER = 'captures'
if len(sys.argv) > 1:
    FOLDER = sys.argv[1]
shutil.rmtree(FOLDER, ignore_errors=True)
os.mkdir(FOLDER)

camera = cv.VideoCapture(0)

if camera.isOpened():
    ret, frame = camera.read()
    if ret:
        print('The image size is: ', frame.shape)
        # more initial info if needed

print('Press ESC to exit the app')
print('Press SPACE to take a photo')

while ret and camera.isOpened():
    key = cv.waitKey(1) & 255 # parse the key pressed
    if key == 27: # ESC
        break
    elif key == 32: # SPACE
        filename = 'capture_%d.png' % COUNTER
        cv.imwrite(filename, frame)
        print('\rPictures taken:', COUNTER, end='')
        COUNTER += 1

camera.release()
cv.destroyAllWindows() # might comment this line