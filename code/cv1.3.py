# %%

import matplotlib.pyplot as plt
import cv2

a = plt.imread('t3.jpg')
size = (768, 512)
dst = cv2.resize(a, size, interpolation=cv2.INTER_CUBIC)  # resize the original img to 768 x 512
plt.imsave('dst.jpg', dst)
plt.imshow(dst)
plt.show()

# %%

(B, G, R) = cv2.split(dst)  # split the RGB channel
b, r, g = B * 0.114, G * 0.587, R * 0.299  # get grayscale img for each of three channel
plt.title('b_grayscale')
plt.imshow(b, cmap='gray')
plt.show()
# %%

plt.title('r_grayscale')
plt.imshow(g, cmap='gray')
plt.show()
# %%

plt.title('g_grayscale')
plt.imshow(r, cmap='gray')
plt.show()
# %%

plt.hist(r.ravel(), 256, [0, 256], density=1)  # plot the histogram of R channel
plt.title('R channel')
plt.show()

# %%

plt.hist(g.ravel(), 256, [0, 256], density=1)  # plot the histogram of G channel
plt.title('G channel')
plt.show()

# %%

plt.hist(b.ravel(), 256, [0, 256], density=1)  # plot the histogram of B channel
plt.title('B channel')
plt.show()

# %%

equ_b = cv2.equalizeHist(B)
equ_g = cv2.equalizeHist(G)
equ_r = cv2.equalizeHist(R)  # equalize the histogram of three channels
equ_dst = cv2.merge([equ_b, equ_g, equ_r])  # merge the equalized channel
plt.subplot(2, 2, 1)
plt.hist(equ_r.ravel(), 256, [0, 256], density=1)
plt.title('R channel')
plt.subplot(2, 2, 2)
plt.title('G channel')
plt.hist(equ_g.ravel(), 256, [0, 256], density=1)
plt.subplot(2, 2, 3)
plt.title('B channel')
plt.hist(equ_b.ravel(), 256, [0, 256], density=1)
plt.subplot(2, 2, 4)
plt.title('Original')
plt.hist(equ_dst.ravel(), 256, [0, 256], density=1)  # plot histogram of RGB channels and merged channel
plt.show()
plt.title('equalized original image')
plt.imshow(equ_dst)
plt.show()
# %%
