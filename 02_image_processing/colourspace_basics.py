# %%
import cv2 as cv
import matplotlib.pyplot as plt
# %%
# Function to display the image
def display_image(img, title='img'):
    while True:
        cv.imshow(title, img)
        if cv.waitKey(10) & 0xFF == 27:
            break
    cv.destroyAllWindows()

# %%
img = cv.imread('../Data/00-puppy.jpg')
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
ogimg = img.copy()
plt.imshow(img)
# %%
# HSV
img = cv.cvtColor(ogimg, cv.COLOR_RGB2HSV)
plt.imshow(img)
# %%
img = cv.cvtColor(ogimg, cv.COLOR_RGB2HLS)
plt.imshow(img)

# %%
