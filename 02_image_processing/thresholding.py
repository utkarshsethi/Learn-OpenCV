# %%
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
# %%
img = cv.imread('../DATA/crossword.jpg', cv.IMREAD_GRAYSCALE)
plt.imshow(img, cmap='gray')
# %%
img.max()
# %%
ret, thresh1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY) # (image, threshold, max_value, threshold_type)
print("ret", ret)
plt.imshow(thresh1, cmap='gray')
# %%
def show_pic(img):
    fig = plt.figure(figsize=(10,10))
    ax = fig.add_subplot(111)
    ax.imshow(img, cmap='gray')
# %%
# show original image
show_pic(img)

# %%
# good threshold value
ret, thresh1 = cv.threshold(img, 150, 255, cv.THRESH_BINARY)
print("ret", ret)
show_pic(thresh1)
# %%
# adaptive thresholding
thresh2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 5, 15)
show_pic(thresh2)
# %%
blended = cv.addWeighted(src1=thresh1, alpha=0.3, src2=thresh2, beta=0.7, gamma=0)
show_pic(blended)
# %%
ret, thresh_blend = cv.threshold(blended, 200, 255, cv.THRESH_BINARY)
print("ret", ret)
show_pic(thresh_blend)
# %%
