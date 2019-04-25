# shear
_EPS = numpy.finfo(float).eps * 4.0
from __future__ import division

import warnings
import math
import numpy
def unit_vector(data, axis=None, out=None):
    if out is None:
        data = numpy.array(data, dtype=numpy.float64, copy=True)
        if data.ndim == 1:
            data /= math.sqrt(numpy.dot(data, data))
            return data
    else:
        if out is not data:
            out[:] = numpy.array(data, copy=False)
        data = out
    length = numpy.atleast_1d(numpy.sum(data*data, axis))
    numpy.sqrt(length, length)
    if axis is not None:
        length = numpy.expand_dims(length, axis)
    data /= length
    if out is None:
        return data
    
def shear_matrix(angle, direction, point, normal):
    normal = unit_vector(normal[:3])
    direction = unit_vector(direction[:3])
    if abs(numpy.dot(normal, direction)) > 1e-6:
        raise ValueError("direction and normal vectors are not orthogonal")
    angle = math.tan(angle)
    M = numpy.identity(4)
    M[:3, :3] += angle * numpy.outer(direction, normal)
    M[:3, 3] = -angle * numpy.dot(point[:3], normal) * direction
    return M

alpha, beta, gamma = 0.123, -1.234, 2.345
origin, xaxis, yaxis, zaxis = (0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)
S_M = shear_matrix(beta, xaxis, origin, zaxis)
print(S_M)

# shear
ZZ = np.concatenate([Z, np.ones((Z.shape[0], 1))], axis=1)
out = np.zeros((8,4))
out = np.dot(S_M, ZZ.T).T[:, :-1]

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
