import numpy as np

POS_IDX = 0
ROT_IDX = 1
SCALE_IDX = 2
COLOR_IDX = 3


def scale(m: np.ndarray, x=1, y=1, z=1):
    if m.shape != (4, 3):
        raise Exception("Matrix must be a [4,3] ndarray")
    r = np.copy(m)
    s = np.array([x, y, z])
    r[SCALE_IDX] = r[SCALE_IDX] * s
    return r


# mmm = np.array([[1, 1, 1], [0, 0, 0], [1, 1, 1], [0, 0, 0]])
# print(mmm)
# print(mmm.shape)
# print()
# mmm = scale(mmm, z=5)
# print(mmm)
#
# print()
# print()
# print()
# a = [1,2,3]
# b = np.array([a,a])
# print(b)


def medians(_shapes):
    rg = []
    shapes = _shapes.copy()
    shapes = np.append(shapes, [shapes[0]], 0)

    for i in range(1, shapes.shape[0]):
        s = np.median([shapes[i - 1, 0], shapes[i, 0]], axis=0)
        rg.append(s)
    return np.array(rg)


# Definitions des 3 points du polygone
a = np.array([[10, 0, 0], [0, 0, 0], [0, 0, 0], [1, 1, 0]])
b = np.array([[-5, 0, 8.66], [0, 0, 0], [0, 0, 0], [0, 1, 1]])
c = np.array([[-5, 0, -8.66], [0, 0, 0], [0, 0, 0], [1, 0, 1]])

positions = np.array([a, b, c])
print(positions.shape)
m = medians(positions)
print(m)

# Calcul des médianes
ab = np.array([a[0], b[0]])
bc = np.array([b[0], c[0]])
ca = np.array([c[0], a[0]])

amx = np.median(ab, axis=0)
amy = np.median(bc, axis=0)
amz = np.median(ca, axis=0)
print("result", amx, amy, amz)
