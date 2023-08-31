#%%
# import OpenCV
import cv2 as cv

#%%
# # Read sample image
img = cv.imread('Resources/Photos/cat.jpg')
print(img)

# display the image
cv.imshow('Sample Image', img)

cv.waitKey(0)  # wait for key press, 0 means wait indefinitely

#%%
# Read video
videoFrame = cv.VideoCapture('Resources\Videos\Sample 144p.mp4')

while True:
    isTrue, frame = videoFrame.read()

    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):   # if 'd' is pressed or 20ms passed, exit
        break

videoFrame.release()
cv.destroyAllWindows()

# %%
