# %%

import numpy as np
import matplotlib.pyplot as plt

a = plt.imread('test.png')
b = np.dot(a[:, :, :3], [0.299, 0.587, 0.114])  # get the grayscale image by formulation
test1 = plt.imshow(b, cmap='gray')
plt.savefig('test1.jpg')
plt.show()

# %%

c = plt.imread('test1.jpg')
d = 255 - c  # To get negative image, use 255 minus original light intensity
plt.subplot(1, 2, 1)
plt.title('Original')
plt.imshow(c)
plt.subplot(1, 2, 2)
plt.title('grayscale_r')
plt.imshow(d)
plt.show()

# %%

import cv2

img = plt.imread('test1.jpg')
row, col = img.shape[0], img.shape[1]  # get the row and col of the original img
M1 = cv2.getRotationMatrix2D((col / 2, row / 2), 180, 1)  # get the rotation matrix
img1 = cv2.warpAffine(img, M1, (col, row))  # rotate img
plt.title('upside down')
plt.imshow(img1)
plt.show()
# %%

R, G, B = a[:, :, 0], a[:, :, 1], a[:, :, 2]  # split RGB channel
R, B = B, R  # swap
e = cv2.merge([R, G, B])  # merge the swapped channel
plt.title('swap the red and blue')
plt.imshow(e)
plt.show()
# %%


a = cv2.imread('test.png', 0)
row, col = a.shape[0], a.shape[1]
M1 = cv2.getRotationMatrix2D((col / 2, row / 2), 180, 1)
b = cv2.warpAffine(a, M1, (col, row))
plt.title('average')
plt.imshow(a + b / 2, cmap='gray')  # average the flipped img and original img
plt.show()
# %%

i = np.random.randint(0, 256, 480 * 640 * 3, 'uint8').reshape(480, 640, 3)  # create a random value between [0,255]
j = (i + c).clip(0, 256)  # clip the intensity above 255
plt.title('random')
plt.imshow(j)
plt.show()
# %%
