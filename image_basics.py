#%%
# imports
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
from PIL import Image

# %%
img = Image.open('DATA/00-puppy.jpg')
print('type(img) = ', type(img))

img_arr = np.asarray(img)

print('img_arr = ', img_arr)

print('type(img_arr) = ', type(img_arr))

print('img_arr.shape = ', img_arr.shape)

plt.imshow(img_arr)

# %%
# channels are RGB

# %%
# show individual channels gray values
print('red channel')
plt.imshow(img_arr[:,:,0], cmap='gray')

#%%
print('green channel')
plt.imshow(img_arr[:,:,1], cmap='gray')

#%%
print('blue channel')
plt.imshow(img_arr[:,:,2], cmap='gray')

# %%
# Red Channel
img_red = img_arr.copy()

img_red[:, :, 1] = 0
img_red[:, :, 2] = 0
plt.imshow(img_red)

# %%
# Green Channel
img_green = img_arr.copy()

img_green[:, :, 0] = 0
img_green[:, :, 2] = 0
plt.imshow(img_green)

# %%
# Blue Channel
img_blue = img_arr.copy()

img_blue[:, :, 0] = 0
img_blue[:, :, 1] = 0
plt.imshow(img_blue)
# %%
