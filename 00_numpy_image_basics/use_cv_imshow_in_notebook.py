# %%
import cv2 as cv

# Load an image from file
img = cv.imread("Data/00-puppy.jpg")

# Show the image
while True:
    cv.imshow("Puppy", img)
    # if cv.waitKey(20) & 0xFF == ord('q'):   # if 'd' is pressed after 20ms passed, exit
    if cv.waitKey(0):
        break
cv.destroyAllWindows()