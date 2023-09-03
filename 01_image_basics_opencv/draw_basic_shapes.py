# %%
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
# %%
blank_img = np.zeros(shape=(512,512,3), dtype=np.uint8)
print("blank_img.shape=",blank_img.shape)
# %%
plt.imshow(blank_img)

# while True:
#     cv.imshow('blank_img', blank_img)
#     if cv.waitKey(0):
#         break
# cv.destroyAllWindows()
# %%
cv.rectangle(blank_img,pt1=(100,400),pt2=(400,100), color=(0,255,0),thickness=5)

plt.imshow(blank_img)
# while True:
#     cv.imshow('blank_img', blank_img)
#     if cv.waitKey(0):
#         break
# cv.destroyAllWindows()
# %%
cv.rectangle(blank_img,pt1=(200,200),pt2=(300,300), color=(255,255,),thickness=-1)

plt.imshow(blank_img)
# while True:
#     cv.imshow('blank_img', blank_img)
#     if cv.waitKey(0):
#         break
# cv.destroyAllWindows()
# %%
cv.circle(img=blank_img,center=(100,100),radius=50,color=(0,0,255),thickness=5)

plt.imshow(blank_img)
# while True:
#     cv.imshow('blank_img', blank_img)
#     if cv.waitKey(0):
#         break
# cv.destroyAllWindows()
# %%
cv.circle(img=blank_img,center=(400,400),radius=50,color=(0,0,255),thickness=-1)

plt.imshow(blank_img)
# while True:
#     cv.imshow('blank_img', blank_img)
#     if cv.waitKey(0):
#         break
# cv.destroyAllWindows()
# %%
cv.line(blank_img,pt1=(0,0),pt2=(512,512),color=(255,255,255),thickness=5)
plt.imshow(blank_img)
# while True:
#     cv.imshow('blank_img', blank_img)
#     if cv.waitKey(0):
#         break
# cv.destroyAllWindows()
# %%
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(blank_img, text="Hello World!", org=(10,500),fontFace=font,fontScale=1,color=(255,255,255),thickness=1,lineType=cv.LINE_AA)
plt.imshow(blank_img)
# %%
# %%
blank_img = np.zeros(shape=(512,512,3), dtype=np.uint8)
# %%
vertices = np.array([[100,300],[200,200],[400,300],[200,400],[250,300]], dtype=np.int32)
print("vertices.shape=",vertices.shape)
# print("vertices", vertices)
vertices = vertices.reshape((-1,1,2))   # check why?
# print("vertices", vertices)
print("vertices.shape=",vertices.shape)
cv.polylines(blank_img, pts=[vertices], isClosed=True, color=(100,100,255), thickness=3)
plt.imshow(blank_img)
# %%
