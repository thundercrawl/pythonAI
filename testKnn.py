import msvcrt as m
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import scipy.misc

# Width and height of each image.
img_size = 32

# Number of channels in each image, 3 channels: Red, Green, Blue.
num_channels = 3

# Length of an image when flattened to a 1-dim array.
img_size_flat = img_size * img_size * num_channels

# Number of classes.
num_classes = 10

def wait():
    if  m.getch() ==b'q':
        exit(0)
    print("recieve char="+str(m.getch()))

def unpickle(file):
    import pickle
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict


def loadimage(raw):
    # Convert the raw images from the data-files to floating-points.
    raw_float = np.array(raw, dtype=float) / 255.0

    print(raw_float)
    # Reshape the array to 4-dimensions.
    images = raw_float.reshape([-1, num_channels, img_size])

    # Reorder the indices of the array.
    images = images.transpose([0,  2, 1])

    return images

def valid_imshow_data(data):
    data = np.asarray(data)
    if data.ndim == 2:
        return True
    elif data.ndim == 3:
        if 3 <= data.shape[2] <= 4:
            return True
        else:
            print('The "data" has 3 dimensions but the last dimension '
                  'must have a length of 3 (RGB) or 4 (RGBA), not "{}".'
                  ''.format(data.shape[2]))
            return False
    else:
        print('To visualize an image the data must be 2 dimensional or '
              '3 dimensional, not "{}".'
              ''.format(data.ndim))
        return False

print("load cifar 10")

dict1 = unpickle(r"C:\projects\ocr\aocr\tensorflow\dataset\cifar-10-batches-py\data_batch_1")

for a in dict1[b'data']:
    single_img_reshaped = np.transpose(np.reshape(a,(3, 32,32)), (1,2,0))
    
    plt.imshow(single_img_reshaped,aspect="auto")
    plt.show()
    scipy.misc.imsave('1.png',single_img_reshaped)
    wait()
    