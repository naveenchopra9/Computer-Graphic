# translation
import warnings
import math
import numpy

def translation_matrix(direction):
    M = numpy.identity(4)
    M[:3, 3] = direction[:3]
    return M
T = translation_matrix((1, 2, 3))
print(T)

# translation
ZZ = np.concatenate([Z, np.ones((Z.shape[0], 1))], axis=1)
out = np.zeros((8,4))
out = np.dot(T, ZZ.T).T[:, :-1]

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
