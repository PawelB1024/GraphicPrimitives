import numpy as np
import matplotlib.pyplot as plt
import math
def elipse(n, m, O, a, b, fill=1, tolerance = 0.1):
    '''
    Funkcja tworząca tablicę RGB i rysująca na niej czworokąt.
    Atrybuty:
        m, n - Rozmiar tablicy m (oś odciętych) na n (oś rzędnych).
        O - Środek elipsy (tupla lub lista).
        a, b - Półosie elipsy.
        fill - Określa czy elipsa ma być wypełniona czy nie (domyślnie 0).
        tolerance - Określa tolerancje na punkty brane za obrys elipsy (domyślnie 0.1).
    Zwraca nowo utworzoną tablice RGB. 
    '''
    assert n > 0 and m > 0, 'Rozmiar tablicy musi być dodatni.'
    assert n > a and m > b, 'środek musi znajdować się w tablicy.'
    def inside(x, y):
        return ((x - O[0]) ** 2) / a ** 2 + ((y - O[1]) ** 2) / b ** 2 <= 1
    def on_boundary(x, y):
        return abs(((x - O[0]) ** 2) / a ** 2 + ((y - O[1]) ** 2) / b ** 2 - 1) < tolerance
    def draw_point(x, y):
        if inside(x, y):
            return (0, 0, 0)
        else:
            return (255, 255, 255)
    image = []
    for i in range(m):
        row = []
        for j in range(n):
            if fill:
                row.append(draw_point(i, j))
            else:
                row.append((0, 0, 0) if on_boundary(i, j) else (255, 255, 255))
        image.append(row)
    return image

rgb = elipse(100, 100, (50, 50), 20, 30, fill=0)
plt.imshow(rgb, interpolation='none', aspect=1)
plt.show()



