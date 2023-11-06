import numpy as np
from  numba import njit
from random import randint
@njit(fastmath=True, cache=True)
def give_height_map(WIDHT, seed=0):
    res = np.full((WIDHT, WIDHT), 0)

    rg = 1
    while rg < WIDHT:
        for xx in range(0, WIDHT, rg):
            for yy in range(0, WIDHT, rg):
                tp = randint(0, 10)
                if tp:
                    for x in range(rg):
                        for y in range(rg):
                            res[xx+x, yy+y] += tp
        rg*=2

    return res

@njit(fastmath=True, cache=True)
def color_height(i):
    if 10 <= i <= 30:
        return [int(238/30*i), int(222/30*i), 0]
    elif 30 < i <= 80:
        return [int(200/80*i), int(200/80*i), int(200/80*i)]
    elif i > 80:
        return [int(255 / 100 * i), int(255 / 100 * i), int(255 / 100 * i)]
    else:
        return [0, 0, int(255 / 10 * i)]


@njit(fastmath=True, cache=True)
def color_map(map):
    res = np.full((len(map), len(map), 3), 0)
    for x in range(len(map)):
        for y in range(len(map)):
            res[x, y] = color_height(map[x, y])
    return res



print(color_map(give_height_map(4096, 1)))

