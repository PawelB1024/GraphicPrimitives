import numpy as np
import matplotlib.pyplot as plt

def circle(x, y, r, fill=False):
    RGB = np.zeros((200, 200, 3), dtype = np.uint8)
    RGB.fill(255)
    for i in range(y-r, y+r+1):
        for j in range (x-r, x+r+1):
            if i >= 200 or j >= 200:
                continue
            xx = j - x
            yy = i - y
            if not fill:
                if xx*xx +yy*yy < r*r+r and xx*xx +yy*yy > r*r-r:
                    RGB[i][j] = 0                
            else:
                if xx*xx + yy*yy < r*r+r:
                    RGB[i][j] = 0   
    return RGB

data = circle(120, 120, 90)
plt.imshow(data, interpolation='none', aspect=1)
plt.show()
data = circle(120, 120, 90, True)
plt.imshow(data, interpolation='none', aspect=1)
plt.show()



def putpixel(RGB, xc, yc):
    try:
        RGB[yc, xc] = 0
    except IndexError:
        pass
def circleB(xc, yc, r, fill=False):
    RGB = np.zeros((200, 200, 3), dtype = np.uint8)
    RGB.fill(255)
    d=3-2*r
    y=r
    i=0
    while i<=y:
        putpixel(RGB, xc-i, yc-y)
        putpixel(RGB, xc-i, yc+y)
        putpixel(RGB, xc+i, yc-y)
        putpixel(RGB, xc+i, yc+y)
        putpixel(RGB, xc-y, yc-i)
        putpixel(RGB, xc-y, yc+i)
        putpixel(RGB, xc+y, yc-i)
        putpixel(RGB, xc+y, yc+i)
        i = i + 1
        if d <= 0:
            d = d+i*4+6
        else:
            d+= 4 * (i - y) + 10
            y-= 1
    return RGB

data = circleB(120, 120, 90)
plt.imshow(data, interpolation='none', aspect=1)
plt.show()



data1 = circle(120, 120, 70)
data2 = circleB(120, 120, 70)
data3 = data1-data2
plt.imshow(data3, interpolation='none', aspect=1)
plt.show()





