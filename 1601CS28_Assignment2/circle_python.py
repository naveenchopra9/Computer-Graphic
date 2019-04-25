import pylab as plt
import numpy as np
from matplotlib.path import Path
from skimage.draw import polygon
img = np.zeros((20, 20), dtype=np.uint8)
r = np.array([2,7,13,13,7,2,2])
c = np.array([3,1,6,11,7,10,3])
rr, cc = polygon(r, c)
img[rr, cc] = 1
img=np.rot90(img)
from matplotlib import pyplot as plt
plt.imshow(img, interpolation='nearest')
plt.show()
