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

rgb = np.zeros((300, 300, 3), dtype=np.uint8)
rgb.fill(255)
start = (10, 10)
end = (270, 250)
thickness = 3
rgb = linePZ(start, end, thickness, rgb) 

plt.imshow(rgb, interpolation='none', aspect=1)
plt.show()



