#shear
%matplotlib inline 
f=()
points = ((100, 100), (200, 100), (200, 200), (100, 200))
w=np.array([[1,0],[2,1]])
for i in points:
    a=i[0]
    b=i[1]
    z=np.array([[a],[b]])
    transformed=np.dot(w,z)    
    z=[transformed[0][0],transformed[1][0]]

    
    z=tuple(z)
    f=f+z
image = Image.new("RGB", (1640, 1480))
draw = ImageDraw.Draw(image)
draw.polygon((f), fill=200)
import matplotlib.pyplot as plt
plt.imshow(image)
    