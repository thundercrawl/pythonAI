import numpy as np
from matplotlib import pyplot as plt

random_image = np.random.random([32, 32])

plt.imshow(random_image, cmap='gray', interpolation='nearest')
plt.show()
plt.savefig("1.png")
print(random_image.__len__())
print(random_image.__class__)
print("show image end")