# %%
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
# %%
bgimg = cv.imread('../data/dog_backpack.png')
bgimg = cv.cvtColor(bgimg, cv.COLOR_BGR2RGB)
plt.imshow(bgimg)
print("bgimg.shape",bgimg.shape)
print("aspect ratio bgimg", bgimg.shape[1]/bgimg.shape[0]) # width/height
# %%
fgimg = cv.imread('../data/watermark_no_copy.png')
fgimg = cv.cvtColor(fgimg, cv.COLOR_BGR2RGB)
plt.imshow(fgimg)
print("fgimg.shape",fgimg.shape)
print("aspect ratio fgimg", fgimg.shape[1]/fgimg.shape[0]) # width/height
# %%
def reload_images():
    bgimg = cv.imread('../data/dog_backpack.png')
    bgimg = cv.cvtColor(bgimg, cv.COLOR_BGR2RGB)
    fgimg = cv.imread('../data/watermark_no_copy.png')
    fgimg = cv.cvtColor(fgimg, cv.COLOR_BGR2RGB)
    return bgimg, fgimg

# %%
######################################## 
# blend images of same size ############
########################################
# %%
# resize fgimg to match bgimg
bgimg = cv.resize(bgimg, (1200, 1200))
fgimg = cv.resize(fgimg, (1200, 1200))
# %%
plt.imshow(bgimg)
print("bgimg.shape",bgimg.shape)
# %%
plt.imshow(fgimg)
print("fgimg.shape",fgimg.shape)
# %%
# blend images
alpha = 0.8
beta = 0.2
blended = cv.addWeighted(src1=bgimg, alpha=alpha, src2=fgimg, beta=beta, gamma=0)
plt.imshow(blended)
# %%
#####################################################
# overlay small image on top of larger image ########
#####################################################
# %%
# 
bgimg, fgimg = reload_images()
fgimg = cv.resize(fgimg, (600, 600))
plt.imshow(fgimg)
print("fgimg.shape",fgimg.shape)
# %%
x_offset = 0
y_offset = 0
x_end = x_offset + fgimg.shape[1] # width of fgimg
y_end = y_offset + fgimg.shape[0] # height of fgimg
# %%overlayed
overlayed = bgimg.copy()
overlayed[y_offset:y_end, x_offset:x_end] = fgimg
plt.imshow(overlayed)
# %%
#####################################################
# using masks #######################################
#####################################################
# %%
bgimg, fgimg = reload_images()
print("bgimg.shape",bgimg.shape)
fgimg = cv.resize(fgimg, (600, 600))
# %%
# create a region of interest (ROI) for the fgimg
rows, cols, channels = fgimg.shape
x_offset = bgimg.shape[1] -cols  # 600 is the width of fgimg
y_offset = bgimg.shape[0] -rows  # 600 is the height of fgimg
roi = bgimg[y_offset:y_offset+rows, x_offset:x_offset+cols]
plt.imshow(roi)
# %%
fggray = cv.cvtColor(fgimg, cv.COLOR_RGB2GRAY)
plt.imshow(fggray, cmap='gray')
# %%
mask_inv = cv.bitwise_not(fggray)
plt.imshow(mask_inv, cmap='gray')
# %%
fg = cv.bitwise_or(fgimg, fgimg, mask=mask_inv)
plt.imshow(fg)
# %%
roi = cv.bitwise_or(roi, fg)
plt.imshow(roi)
# %%
blended = bgimg.copy()
blended[y_offset:y_offset+rows, x_offset:x_offset+cols] = roi
plt.imshow(blended)
# %%
