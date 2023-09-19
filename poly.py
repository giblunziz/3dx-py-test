import json
import math

n = 8
angle = math.radians(360 / n)
longueur = 2 * math.sin(angle/2)
print(n, angle)

for i in range(n):
    px = round(math.cos(angle * i), 2)
    py = round(math.sin(angle * i), 2)
    pz = 0
    P = [px, py, pz]

    rx = 0.
    ry = round(math.degrees(angle * i),2)
    rz = 0.
    R = [rx, ry, rz]

    sx = 1.
    sy = round(longueur,2)
    sz = 1.
    S = [sx,sy,sz]


    box = {
        "n": "Box",
        "p": P,
        "r": R,
        "s": S
    }
    print(json.dumps(box))

