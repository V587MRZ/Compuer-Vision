import math
import numpy as np
import cv2


class Rotation:
    def __init__(self, src, theta):
        self.src = src
        self.theta = theta
        self.x0 = 256
        self.y0 = 256  # center of the rotation
        self.row, self.col = self.src.shape  # the height and width of img
        self.For = np.zeros((self.row, self.col), dtype="uint8")  # blank img for forward mapping
        self.Back = np.zeros((self.row, self.col), dtype="uint8")  # blank img for inverse mapping
        self.demo()

    def my_rotate(self):
        for i in range(self.row):
            for j in range(self.col):
                # the original position multiply the rotation matrix, and add the position of  center to adjust position on new img
                u = (i - self.x0) * math.cos(self.theta * math.pi / 180) + (j - self.y0) * -math.sin(
                    self.theta * math.pi / 180) + self.x0
                v = (i - self.x0) * math.sin(self.theta * math.pi / 180) + (j - self.y0) * math.cos(
                    self.theta * math.pi / 180) + self.y0
                # if there are no corresponding position on new coordinate, copy the nearliest pixels
                u, v = int(u), int(v)
                # fill in the blank img
                if u < self.row and v < self.col:
                    self.For[i, j] = self.src[u, v]
                # because the inverse mapping change the destined position to original position, use negative angle to instead angle
                self.theta_r = -self.theta
                # the original position multiply the rotation matrix, and add the position of  center to adjust position on new img
                x = (i - self.x0) * math.cos(self.theta_r * (math.pi / 180)) + (j - self.y0) * math.sin(
                    self.theta_r * (math.pi / 180)) + self.x0
                y = (i - self.x0) * -math.sin(self.theta_r * (math.pi / 180)) + (j - self.y0) * math.cos(
                    self.theta_r * (math.pi / 180)) + self.y0
                x, y = int(x), int(y)
                if x < self.row and y < self.col:  # delete the new position which is out of the blank img
                    self.Back[i, j] = self.src[x, y]
                    continue

    def demo(self):
        self.my_rotate()  # execute the above function
        cv2.imshow(str(self.theta) + ' degree forward', self.For)
        cv2.imshow(str(self.theta) + ' degree backward', self.Back)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


a = cv2.imread('test.png', 0)  # test the different rotation
theta90 = Rotation(a, 90)
theta45 = Rotation(a, 45)
theta_15 = Rotation(a, -15)
theta_45 = Rotation(a, -45)
theta_90 = Rotation(a, -90)
