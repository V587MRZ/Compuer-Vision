# %%

import math
import numpy as np
import matplotlib.pyplot as plt

a = plt.imread('t4.JPG')
b = np.dot(a[:, :, :3], [0.299, 0.587, 0.114])  # get the grayscale image
plt.subplot(1, 2, 1)
plt.title('Grayscale')
plt.imshow(b, cmap='gray')
plt.imsave('gray.jpg', b, cmap='gray')
plt.subplot(1, 2, 2)
plt.title('Original')
plt.imshow(a)
plt.show()
# %%
c = 15 * np.random.randn(256,
                         256) + b  # get the Gaussian noise with zero mean, and standard deviation of 15 and add it on original img
plt.title('Gaussian noise')
plt.imshow(c, cmap='gray')
plt.show()
# %%

plt.subplot(2, 1, 1)
plt.hist(b.flatten(), 256, density=1)
plt.title('Original')
plt.subplot(2, 1, 2)
plt.hist(c.flatten(), 256, density=1)  # plot the histogram of both two img
plt.title('Gaussian noise')
plt.show()

# %%


class my_gauss_filter:
    def __init__(self, src, size, sigma=1.0):
        self.size = size  # create attributes and methods
        self.src = src
        self.sigma = sigma
        self.h, self.w, self.sum = 0, 0, 0
        self.kernel = np.zeros((size, size), np.float32)
        self.dst = np.array([0])
        self.gauss_kernel()
        self.get_size()
        self.my_gauss_filter()

    def gauss_kernel(self):
        for i in range(self.size):
            for j in range(self.size):
                norm = math.pow(i - 1, 2) + pow(j - 1, 2)
                self.kernel[i, j] = math.exp(-norm / (2 * math.pow(self.sigma, 2)))  # Gaussian function
        sum = np.sum(self.kernel)  # sum the applied pixels
        self.kernel = self.kernel / sum  # divided by sum to get Gaussian filter
        return

    def get_size(self):
        self.h, self.w = self.src.shape[0], self.src.shape[1]  # get the width and height of source img
        self.dst = np.zeros((self.h, self.w))  # create a blank ndarray
        return

    def my_gauss_filter(self):
        for i in range(self.h - 4):
            for j in range(self.w - 4):
                self.sum = 0
                for k in range(5):
                    for l in range(5):
                        self.sum += self.src[i + k, j + l] * self.kernel[k, l]  # Convolution
                self.dst[i + 2, j + 2] = self.sum  # put convoluted pixels to the blank ndarray
        return plt.imshow(self.dst, cmap='gray')  # plot de-noised img


# %%

plt.subplot(2, 2, 1)
exp1 = my_gauss_filter(c, 5, sigma=1)  # test the different standard deviation
plt.title('sigma=1')
plt.subplot(2, 2, 2)
exp6 = my_gauss_filter(c, 5, sigma=6)
plt.title('sigma=6')
plt.subplot(2, 2, 3)
exp11 = my_gauss_filter(c, 5, sigma=11)
plt.title('sigma=11')
plt.subplot(2, 2, 4)
exp16 = my_gauss_filter(c, 5, sigma=16)
plt.title('sigma=16')
plt.show()

# %%

import cv2

plt.subplot(1, 2, 1)
d = cv2.GaussianBlur(c, (5, 5), 1)  # in-build function of Gaussian filter
plt.title('inbuilt function')
plt.imshow(d, cmap='gray')
plt.subplot(1, 2, 2)
plt.title('my_gauss_filter')
exp1 = my_gauss_filter(c, 5, sigma=1)  # compare my function and buildin function
plt.show()
# %%
