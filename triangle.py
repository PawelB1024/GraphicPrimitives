import numpy as np
import matplotlib.pyplot as plt
import math
def linePZ(P1, P2, d, RGB, color = (0, 0, 0)):
    '''
    Funkcja rysująca odcinek na tablicy RGB.
    Jeżeli ze względu na grubość linii twój odcinek wykroczy poza tablice to funkcja pominie punkty które wykraczają.
    
    Atrybuty:
        P1, P2 - Punkty linii zawierające współrzędne (x, y) typu int.
        d (int)- Grubość linii typu int, grubość nie może być mniejsza od 1.
        RGB - Tablica pikseli o typie Numpy uint8, w której rysowana jest linia.
        color - Kolor linii w rgb domyślnie (0, 0, 0) (kolor czarny).
    
    Zwraca tablice przyjętą tablice RGB.
    '''
    assert P1[0] >= 0 and P1[1] >= 0 and P2[0] >= 0 and P2[1] >= 0, "Punkty muszą mieć dodatnie współrzędne."
    assert P1[0] < RGB.shape[0] and P2[0] < RGB.shape[0] and \
            P1[1] < RGB.shape[1] and P2[1] < RGB.shape[1], "Wspołrzędne punktów nie mogą wykraczać poza tablice."
    assert d > 0, "Grubość linii musi być dodatnia."
    if P1 == P2:
        RGB[P1[1], P1[0]] = color
        return RGB
    y1, x1 = P1
    y2, x2 = P2
    dx, dy = x2 - x1, y2 - y1
    length = math.ceil((np.sqrt(dx**2 + dy**2)))
    dx, dy = dx / length, dy / length
    for i in range(length):
        x, y = x1 + i * dx, y1 + i * dy
        for d_x in range(-d // 2, d // 2):
            for d_y in range(-d // 2, d // 2):
                if x + d_x < 0 or y + d_y < 0:
                    continue
                try:
                    RGB[int(x + d_x), int(y + d_y)] = color
                except IndexError:
                    pass
    return RGB

def dist(x1, y1, x2, y2):
    return math.sqrt(math.pow((x2-x1), 2)+math.pow((y2-y1), 2))

def heron(a, b, c):
    p = (a + b + c)/2
    try:
        return math.sqrt(p*(p-a)*(p-b)*(p-c))
    except:
        return 0
def triangle(data, a, b, c, color):
    linePZ((a[0],a[1]), (b[0], b[1]), 2, data, color)
    linePZ((a[0], a[1]), (c[0], c[1]), 2, data, color)
    linePZ((b[0], b[1]), (c[0], c[1]), 2, data, color)
    xmin = a[0]
    xmax = a[0]
    ymin = a[1]
    ymax = a[1]
    for el in [a[0], b[0], c[0]]:
        if el > xmax:
            xmax = el
        elif el < xmin:
            xmin = el
    for el in [a[1], b[1], c[1]]:
        if el > ymax:
            ymax = el
        elif el < ymin:
            ymin = el
    pole = heron(dist(a[0], a[1], b[0], b[1]), dist(a[0], a[1], c[0], c[1]), dist(b[0], b[1], c[0], c[1]))
    for i in range(xmin, xmax+1):
        for j in range(ymin, ymax+1):
            pole1 = heron(dist(a[0], a[1], b[0], b[1]), dist(i, j, a[0], a[1]), dist(i, j, b[0], b[1]))
            pole2 = heron(dist(a[0], a[1], c[0], c[1]), dist(i, j, a[0], a[1]), dist(i, j, c[0], c[1]))
            pole3 = heron(dist(b[0], b[1], c[0], c[1]), dist(i, j, b[0], b[1]), dist(i, j, c[0], c[1]))
            if pole1 + pole2 + pole3 <= pole+1:
                data[j, i] = color
    return pole

def generate_bg(size):
    data = np.zeros((size, size, 3), dtype=np.uint8)
    data.fill(255)
    return data 
data = generate_bg(300)
triangle(data, (50, 50), (100, 100), (150, 50), (0, 0, 0))
plt.imshow(data, interpolation='none', aspect=1)
plt.show()

