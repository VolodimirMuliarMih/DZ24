#giometric ratio
import numpy as np
import pandas as pd

def geometric_series_generator(x, r, n):
    """Геометрическая прогрессия, r- знаменатель геометрической прогресси,
    n - длинна ряда,
    """

    for i in range(n):
        yield x
        x = x*r

N = 10
N0 = 1
r = 2
gen = geometric_series_generator(N0, r, N)
geom_series = np.fromiter(gen, int, count=N)#создаеv одномерный массив из итерируемого объекта(N), вместо int можно и float
print(pd.Series(geom_series, index=np.arange(0, N, 1)))
