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

# Definitions des 3 points du polygone
a = np.array([10,0])
b = np.array([-5,8.66])
c = np.array([-5,-8.66])

# Calcul des médianes
ab = np.array([a,b])
bc = np.array([b,c])
ca = np.array([c,a])

amx = np.median(ab, axis=0)
amy = np.median(bc, axis=0)
amz = np.median(ca, axis=0)
print(amx, amy, amz)