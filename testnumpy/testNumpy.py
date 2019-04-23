
import numpy as np


import matplotlib.pyplot as plt

def showArrayImage():
    a = np.array([1,2,3,4,5])
    a = np.expand_dims(a, axis=0)  # or axis=1
    plt.imshow(a)
    plt.show()


def numpysum(n):
  a = np.arange(n) ** 2
  print(a)
  b = np.arange(n) ** 3
  print(b)
  c = a + b
  return c


def testdoubleStar():
    
    print("2**3="+str(2**3))

#narray n-dimension array
#np.arrange(36).reshape(3,4,3) 3D array
def createN_DArray():
  print("------auto filled ND array-------")
  print(np.arange(100*1*2).reshape(100,1,2))
  print("------auto filled nD array-------")

def createD2Array():
    b = np.arange(24).reshape(4,3,2)
    b.shape
    print(b)
    print(b.shape)
def listMore(more=list):
    print(more.__class__.__name__)



def npm1():

    a1=np.arange(24).reshape(4,3,2)
    v1 = np.array([1, 2, 3])
    print(v1.shape)
    v2 = 0.5 * v1

    print(np.linalg.norm(a1))
    print(v2)
    print(np.arccos(v1.dot(v2) / (np.linalg.norm(v1) * 
           np.linalg.norm(v2))))

#main bb here

createN_DArray()
