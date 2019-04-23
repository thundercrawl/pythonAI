import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures


x = np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1))
print(x)
y = np.array([15, 11, 2, 8, 25, 32])