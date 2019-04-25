from graphics import *
window = GraphWin("Circle", 1920, 1080)

rect = Rectangle(Point(200, 100), Point(100, 200))
rect.draw(window)


import PIL.ImageDraw as ImageDraw
import PIL.Image as Image



draw = ImageDraw.Draw(image)

# points = ((1,1), (2,1), (2,2), (1,2), (0.5,1.5))


draw.polygon((points), fill=200)

image.show()
