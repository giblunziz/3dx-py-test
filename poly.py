import json
import math

segments=8
angle = math.radians(360 / segments)
longueur = 2 * math.sin(angle / 2)
print(segments, angle)


def getPolyObject(segment, radius):
    px = round(math.cos(angle * segment), 2)
    py = round(math.sin(angle * segment), 2)
    pz = 0
    P = [px, py, pz]

    rx = 0.
    ry = round(math.degrees(angle * segment), 2)
    rz = 0.
    R = [rx, ry, rz]

    sx = 1.
    sy = round(longueur, 2)
    sz = 1.
    S = [sx, sy, sz]

    C = [1., 0., .5]

    box = {
        "n": "Box",
        "p": P,
        "r": R,
        "s": S,
        "c": C
    }
    return box


def poly(segments: 8, radius: 10):
    for i in range(segments):
        box = getPolyObject(segment=i, radius=radius)
        print(json.dumps(box))


if __name__ == '__main__':
    poly(8)
