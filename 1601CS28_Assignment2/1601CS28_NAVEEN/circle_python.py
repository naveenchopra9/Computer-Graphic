import matplotlib.pyplot as plt
from skimage import draw
arr = np.zeros((200, 200))
rr, cc = draw.circle_perimeter(100, 100, radius=80, shape=arr.shape)
arr[rr, cc] = 1
plt.imshow(arr)
plt.show()