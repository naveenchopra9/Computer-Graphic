# scale
_EPS = numpy.finfo(float).eps * 4.0
from __future__ import division

import warnings
import math
import numpy
def scale_matrix(factor, origin=None, direction=None):
    if direction is None:
        M = numpy.array(((factor, 0.0,    0.0,    0.0),
                         (0.0,    factor, 0.0,    0.0),
                         (0.0,    0.0,    factor, 0.0),
                         (0.0,    0.0,    0.0,    1.0)), dtype=numpy.float64)
        if origin is not None:
            M[:3, 3] = origin[:3]
            M[:3, 3] *= 1.0 - factor
    else:
        direction = unit_vector(direction[:3])
        factor = 1.0 - factor
        M = numpy.identity(4)
        M[:3, :3] -= factor * numpy.outer(direction, direction)
        if origin is not None:
            M[:3, 3] = (factor * numpy.dot(origin[:3], direction)) * direction
    return M
origin, xaxis, yaxis, zaxis = (0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)
S = scale_matrix(1.23, origin)
print(S)

# scale
ZZ = np.concatenate([Z, np.ones((Z.shape[0], 1))], axis=1)
out = np.zeros((8,4))
out = np.dot(S, ZZ.T).T[:, :-1]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

r = [-1,1]

X, Y = np.meshgrid(r, r)
# plot vertices
ax.scatter3D(out[:, 0], out[:, 1], out[:, 2])

# list of sides' polygons of figure

verts = [[out[0],out[1],out[2],out[3]],
 [out[4],out[5],out[6],out[7]], 
 [out[0],out[1],out[5],out[4]], 
 [out[2],out[3],out[7],out[6]], 
 [out[1],out[2],out[6],out[5]],
 [out[4],out[7],out[3],out[0]]]

# plot sides
ax.add_collection3d(Poly3DCollection(verts, 
 facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
