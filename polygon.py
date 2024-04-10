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

def point_in_polygon(x, y, vertices):
    '''
    Algorytm point in polygon (PIP). Sprawdza czy punkt jest wewnątrz wielokąta.
    
    Atrybuty:
        x, y - Współrzędne punktu do sprawdzenia.
        vertices - Lista krotek z punktami opisującymi wielokąt.
    
    Zwraca True jeżeli punkt znajduje się w wielokącie, False w innym przypadku.
    '''
    n = len(vertices)
    inside = False
    p1x, p1y = vertices[0]
    for i in range(1, n + 1):
        p2x, p2y = vertices[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y
    return inside

def fill_poly(image, vertices, color):
    '''
    Funkcja rysująca wypełniony czworokąt. Korzysta z algorytmu PIP.
    
    Atrybuty:
        image - Tablica RGB w której rysowany będzie czworokąt
        vertices - Lista punktów (krotek) opisujących czworokąt.
        color - Kolor jakim narysowany zostanie czworokąt.
    
    Zwraca None
    '''
    x_min = min(x for x, y in vertices)
    x_max = max(x for x, y in vertices)
    y_min = min(y for x, y in vertices)
    y_max = max(y for x, y in vertices)
    for x in range(x_min, x_max + 1):
        for y in range(y_min, y_max + 1):
            if point_in_polygon(x, y, vertices):
                image[y, x] = color

def quadrilateral(m, n, P1, P2, P3, P4, fill = 0, color = (0, 0, 0)):
    '''
    Funkcja tworząca tablicę RGB i rysująca na niej czworokąt.
    Atrybuty:
        m, n - Rozmiar tablicy m (oś odciętych) na n (oś rzędnych).
        P1, P2, P3, P4 - Punkty opisujące czworokąt w postaci współrzędnych (x, y).
        fill - Określa czy czworokąt ma być wypełniony czy nie (domyślnie 0).
        color - Określa kolor czworokąta (domyślnie kolor czarny(0, 0, 0)).
    Zwraca nowo utworzoną tablice RGB. 
    '''
    vertices = [P1, P2, P3, P4]
    for P in vertices:
        if P[0] >= m or P[1] >= n or P[0] < 0 or P[1] < 0:
            raise Exception("Punkty opisujące czworokąt nie mogą wychodzić poza tablice.")
    image = np.zeros((n, m, 3), dtype=np.uint8)
    image.fill(255)
    if fill:
        fill_poly(image, vertices, color)
    else:
        for i in range(-1, len(vertices) - 1):
            x1, y1 = vertices[i]
            x2, y2 = vertices[i + 1]
            linePZ((x1, y1), (x2, y2), math.ceil(math.ceil(m+n//2)/300)-1, image, color)
    return image
            

P1 = (200, 50)
P2 = (225, 150)
P3 = (150, 250)
P4 = (110, 250)


image = quadrilateral(300, 300, P1, P2, P3, P4, fill = 1)

plt.imshow(image)
plt.show()