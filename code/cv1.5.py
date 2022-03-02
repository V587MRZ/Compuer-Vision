import matplotlib.pyplot as plt
import cv2
import numpy as np

# %%

a = cv2.imread('t4.JPG', 0)  # read the image


def my_Sobel_filter(src, op):
    Mx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])  # sobel filter in x axis
    My = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])  # sobel filter in y axis
    dst = np.zeros_like(src)
    for i in range(254):
        for j in range(254):
            my_sum = 0
            for k in range(3):
                for l in range(3):
                    if op == 'vertical':
                        my_sum += (src[i + k, j + l] * Mx[k, l])  # Convolution
                    else:
                        my_sum += (src[i + k, j + l] * My[k, l])
            dst[i + 1, j + 1] = abs(my_sum)  # put convoluted pixels to the blank ndarray
    return plt.imshow(dst, cmap='gray')  # plot de-noised img


my_Sobel_filter(a, 'horizontal')
plt.title('my horizontal Sobel filter')
plt.show()
# %%

b = cv2.Sobel(a, cv2.CV_64F, 0, 1, ksize=3)
c = cv2.Sobel(a, cv2.CV_64F, 1, 0, ksize=3)
plt.subplot(1, 2, 1)
plt.title('in build vertical Sobel filter')
plt.imshow(c, cmap='gray')
plt.subplot(1, 2, 2)
plt.title('my vertical Sobel filter')
my_Sobel_filter(a, 'vertical')
plt.show()
plt.subplot(1, 2, 1)
plt.title('in build horizontal Sobel filter')
plt.imshow(b, cmap='gray')
plt.subplot(1, 2, 2)
plt.title('my horizontal Sobel filter')
my_Sobel_filter(a, 'horizontal')  # compare the build-in function and my function
plt.show()
