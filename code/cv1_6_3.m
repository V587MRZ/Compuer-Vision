clear
img = imread('test.png')
img_r1 = imrotate(img,45,'nearest','loose')
img_r2 = imrotate(img,45,'bilinear','loose')
img_r3 = imrotate(img,45,'bicubic','loose')
imwrite(img_r1,'nearest.jpg')
imwrite(img_r2,'bilinear.jpg')
imwrite(img_r3,'bicubic.jpg')