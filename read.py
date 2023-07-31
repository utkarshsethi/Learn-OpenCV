# import OpenCV
import cv2 as cv

# # Read sample image
# img = cv.imread('Photos/sample1.jpg')

# # display the image
# cv.imshow('Sample Image', img)

# # wait for key press
# cv.waitKey(0)

# Read video
video = cv.VideoCapture('Videos/Sample 144p.mp4')

while True:
    isTrue, frame = video.read