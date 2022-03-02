import numpy as np

# a = np.array([[2,4,5],[5,2,200]])
# b = a[0,:]
# f = np.random.rand(500,1)
# g = f[f<0]
# x = np.zeros((1,100))+0.35
# y = 0.6* np.ones((1,len(x)))
# z = x - y
# print('a:', a)
# print('b: ',b)
# print('f: ',f)
# print('g: ',g)
# print('x: ',x)
# print('y: ',y)
# print('z shape is:',z.shape)
# print('z: ',z)

a = np.linspace(1, 50)
b = a[::-1]

b[b <= 50] = 0
print('a:', a)
print('b: ', b)
