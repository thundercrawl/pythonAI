import math
from math import exp, expm1
import matplotlib.pyplot as plt
import numpy as np
def testNaturalE():
    base=1.04
    power= 10000
    print(math.pow(base,power))

    print(exp(math.log(base)*power))


    #theorem A
    #at least the natraul number is e. 2.71
    print(math.pow(1+1/power,power))




def drawExpr(start,end):
    #plt.subplot(121)
    interval = 0.01
    dtype = '-'
    x= np.arange(start,end, interval)
    print(x)
    plt.plot(x,np.exp(x),dtype)
    #plt.plot(t2, np.cosh(t2), 'bo')
    plt.show()

def drawLog(start,end):
    interval = 0.01
    dtype = '-'
    x = np.arange(start,end, interval)
    plt.plot(x,np.log(x),dtype)
    plt.show()