import cv2 as cv
import numpy as np

# Define a global variables
color = (0, 255, 0)
isDrawing = False
ix = -1
iy = -1



# mouse callback function
def draw_on_image(event, x, y, flags, param):
    global ix, iy, isDrawing, color

    # events
    # drawing
    if event == cv.EVENT_LBUTTONDOWN:
        isDrawing = True
        ix, iy = x, y
    elif event == cv.EVENT_MOUSEMOVE:
        if isDrawing:
            cv.circle(img=img, center=(x,y), radius=0, color=color, thickness=-1)
    elif event == cv.EVENT_LBUTTONUP:
        isDrawing = False
    
    # color
    elif event == cv.EVENT_RBUTTONDOWN:
        color = (0, 0, 255)
    elif event == cv.EVENT_RBUTTONUP:
            color = (0, 255, 0)

    # clear
    elif event == cv.EVENT_MBUTTONDOWN:
        img[:] = 0



# Create a black image, a window and bind the function to window
cv.namedWindow(winname='my_drawing')
cv.setMouseCallback('my_drawing', draw_on_image)



# display the image
# Function to display the image
def display_image(img, title='img'):
    while True:
        cv.imshow(title, img)
        if cv.waitKey(10) & 0xFF == 27:
            break
    cv.destroyAllWindows()

img = np.zeros((512,512,3), np.uint8)
print("img.shape=",img.shape)
print("img.dtype=",img.dtype)
display_image(img, 'my_drawing')