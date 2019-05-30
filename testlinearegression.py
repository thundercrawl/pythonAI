import numpy as np
from sklearn.linear_model import LinearRegression


x = np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1))
print(x)
y = np.array([15, 11, 2, 8, 25, 32])

#create random matrix
#create the sample by init process in a json file
sample = np.random.normal(loc=[2., 20.], scale=[1., 3.5],size=(12,3, 2))
print(sample)

#axis refer to a single dimension of multidimension array
#provide multi array math operation
arr = np.array([[1, 2, 3],
               [20, 20, 20]])
print(arr.sum(axis=1))
print(arr.mean(axis=1))
mu=arr.mean(axis=1)
print('sample:', sample.shape, '| means:', mu.shape)
print(arr.std(axis=1))

#array operation
print(np.log(np.array([1,2,3])))

print(np.random.randn(1, 10))