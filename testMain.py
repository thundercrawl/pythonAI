from bv.util import logger as log
import numpy as np
from scipy.misc import imread, imsave, imresize
import matplotlib.pyplot as plt

log.log_file_path="c:/trace.log"
log.loginfo(" start loading image")


def showImageTest():
    img = imread("./1.png")

    a1 = np.array([[ 1., 2., 3.],
    [ 4., 5., 6.]])
    a2 = a1*[0.1,0.2,0.3]


    print(np.array([0, 0, 0]).dtype,np.uint8)
    print(a2)
    print(a2.dtype,a2.shape)
    print(np.arange(0,10,2))
    print(img.dtype, img.shape) 

    log.loginfo(img)
    log.loginfo("show image")
    plt.imshow(img)
    plt.show()

showImageTest()