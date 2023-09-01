import cv2 as cv

# Resizing function


def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)     # frame.shape[1] is the width
    height = int(frame.shape[0] * scale)    # frame.shape[0] is the height
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


# Read image and rescale
img = cv.imread('Photos/sample1.jpg')
img_resized = rescaleFrame(img, 0.25)
cv.imshow('Sample Image', img)
cv.imshow('Rescaled Image', img_resized)

# Read video and rescale
videoFrame = cv.VideoCapture('Videos/Sample 144p.mp4')

while True:
    isTrue, frame = videoFrame.read()

    frame_resized = rescaleFrame(frame)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):   # if 'd' is pressed or 20ms passed, exit
        break

videoFrame.release()
cv.destroyAllWindows()
