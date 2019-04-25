import numpy as np
import cv2
# Create a black image
img = np.zeros((720,720,3), np.uint8)

#################       LINE        #########################

cv2.line(img,(20,600),(600,600),(255,255,153),2)

# Draw a diagonal blue line with thickness of 2 px
# Parameters: 
# img – Image where the circle is drawn
# center– Center of the circle
# radius - Radius of the circle
# color - Circle color
# thickness -Thickness of the circle outline if positive, otherwise this indicates that a filled circle 
# lineType – Type of the circle boundary
# shift – Number of fractional bits in the center coordinates and radius value

#################    RECTANGLE       #########################

cv2.rectangle(img,(400,103),(610,303),(225, 31, 87),3)

# top-left corner and bottom-right corner of rectangle.

#################      CIRCLE        #########################

cv2.circle(img,(300,103), 70, (255,255,0), -1)

# center coordinates and radius

#################      ELLIPSE          #########################

cv2.ellipse(img,(156,256),(100,50),0,0,180,255,-1)

# One argument is the center location
# Next argument is axes lengths (major axis length, minor axis length)
# Angle is the angle of rotation of ellipse in anti-clockwise direction
# startAngle and endAngle denotes the starting and ending of ellipse arc measured in clockwise direction from major axis

#################     POLAYLINE       #########################

pts = np.array([[20,10],[90,50],[120,150],[150,60],[180,20],[110,5]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(0,255,255))

#################      Adding Text       #########################

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'polyline',(40,40), font, 1,(0, 0, 255),2,cv2.LINE_AA)
cv2.putText(img,'circle',(250,103), font, 1,(0, 0, 255),2,cv2.LINE_AA)
cv2.putText(img,'rectangle',(420,200), font, 1,(0, 0, 255),2,cv2.LINE_AA)
cv2.putText(img,'line',(200,570), font, 1,(0, 0, 255),2,cv2.LINE_AA)
cv2.putText(img,'ellipse',(156,336), font, 1,(0, 0, 255),2,cv2.LINE_AA)
cv2.imwrite("square_circle_opencv.jpg", img)
