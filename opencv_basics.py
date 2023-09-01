# %%
import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
# %%
img = cv.imread('DATA/00-puppy.jpg')
print('type(img):', type(img))
print('img.shape:', img.shape)

# display usign matplotlib
plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))

img_plt = cv.cvtColor(img, cv.COLOR_BGR2RGB) # convert to RGB

# display the image
# doesn't work in Jupyter Notebook
# cv.imshow('Sample Image', img)
# cv.waitKey(10)  # wait for key press for 10ms
# cv2.destroyAllWindows()  # close all windows
# %%
# convert to grayscale
fig = plt.figure(figsize=(10, 5)) # width, height

img_lenna = cv.imread('Resources/Photos/Lenna.png')
print('img_lenna.shape:', img_lenna.shape)
ax = fig.add_subplot(121) # 1 row, 1 column, 1st plot
ax.imshow(cv.cvtColor(img_lenna, cv.COLOR_BGR2RGB))

img_lenna_gray = cv.imread('Resources/Photos/Lenna.png', cv.IMREAD_GRAYSCALE)
print('img_lenna_gray.shape:', img_lenna_gray.shape)
ax = fig.add_subplot(122) # 1 row, 1 column, 1st plot
ax.imshow(img_lenna_gray, cmap='gray')

# %%
fig = plt.figure(figsize=(10, 5)) # width, height

ax = fig.add_subplot(121) # 1 row, 1 column, 1st plot
ax.imshow(img_plt)

# resize the image
print('shape=', img_plt.shape)
img_resized = cv.resize(img_plt, (640, 480)) # (width, height)
ax = fig.add_subplot(122) # 1 row, 1 column, 2nd plot
ax.imshow(img_resized)

# %%
# resize using ratio
w_ratio = 0.8   # 80% of the original width
h_ratio = 0.2   # 20% of the original height
img_resized_ratio = cv.resize(img_plt, (0, 0), img_plt, w_ratio, h_ratio) # cv.resize(src, dsize[, dst[, fx[, fy[, interpolation]]]])
plt.imshow(img_resized_ratio)

# %%
# flip the image
fig = plt.figure(figsize=(10, 5)) # width, height
ax = fig.add_subplot(121) # 1 row, 1 column, 1st plot
ax.imshow(img_plt)
ax.set_title('Original Image')

img_flip = cv.flip(img_plt, -1) # 0: flip vertically, 1: flip horizontally, -1: flip both vertically and horizontally
ax = fig.add_subplot(122) # 1 row, 1 column, 2nd plot
ax.imshow(img_flip)
ax.set_title('Flipped Image')

# %%
type(img_plt)
# cv.imwrite('./tmp.jpg', cv.cvtColor(img_plt, cv.COLOR_RGB2BGR))