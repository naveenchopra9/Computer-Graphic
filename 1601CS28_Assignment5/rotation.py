# rotation
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
def quaternion_matrix(quaternion):
    q = numpy.array(quaternion, dtype=numpy.float64, copy=True)
    n = numpy.dot(q, q)
    if n < _EPS:
        return numpy.identity(4)
    q *= math.sqrt(2.0 / n)
    q = numpy.outer(q, q)
    return numpy.array([
        [1.0-q[2, 2]-q[3, 3],     q[1, 2]-q[3, 0],     q[1, 3]+q[2, 0], 0.0],
        [    q[1, 2]+q[3, 0], 1.0-q[1, 1]-q[3, 3],     q[2, 3]-q[1, 0], 0.0],
        [    q[1, 3]-q[2, 0],     q[2, 3]+q[1, 0], 1.0-q[1, 1]-q[2, 2], 0.0],
        [                0.0,                 0.0,                 0.0, 1.0]])

def random_quaternion(rand=None):
    if rand is None:
        rand = numpy.random.rand(3)
    else:
        assert len(rand) == 3
    r1 = numpy.sqrt(1.0 - rand[0])
    r2 = numpy.sqrt(rand[0])
    pi2 = math.pi * 2.0
    t1 = pi2 * rand[1]
    t2 = pi2 * rand[2]
    return numpy.array([numpy.cos(t2)*r2, numpy.sin(t1)*r1,
                        numpy.cos(t1)*r1, numpy.sin(t2)*r2])
def random_rotation_matrix(rand=None):
    return quaternion_matrix(random_quaternion(rand))

alpha, beta, gamma = 0.123, -1.234, 2.345
origin, xaxis, yaxis, zaxis = (0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)
R = random_rotation_matrix(numpy.random.rand(3))
print(R)

# rotation
ZZ = np.concatenate([Z, np.ones((Z.shape[0], 1))], axis=1)
out = np.zeros((8,4))
out = np.dot(R, ZZ.T).T[:, :-1]

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
