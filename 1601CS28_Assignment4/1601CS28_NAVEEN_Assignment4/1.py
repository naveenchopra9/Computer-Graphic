import graphics
xc = 985
yc = 540


def draw_pixel(window, x, y):
    x=x*1.5
    y=y*2.5+5
    window.plot(xc+x, yc+y, 'black')
    window.plot(xc+x, yc-y, 'black')
    window.plot(xc+y, yc+x, 'black')
    window.plot(xc+y, yc-x, 'black')
    window.plot(xc-x, yc-y, 'black')
    window.plot(xc-y, yc-x, 'black') 
    window.plot(xc-x, yc+y, 'black')
    window.plot(xc-y, yc+x, 'black')
def drawCircle(window, r):
    x = 0
    y = r
    p = 1 - r 
    draw_pixel(window, x, y)
    while x <= y:
        if (p < 0): 
            p = p + 2 * x + 3
        else:
            p = p + 2 * (x - y) + 5
            y-=1
        x+=1
        draw_pixel(window, x, y)
    window.getMouse()
    window.close()
window = GraphWin("Circle", 1920, 1080)
window.setBackground('white')
radius = 100
drawCircle(window, radius)
