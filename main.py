import json
import math

data = {}

BLACK = [.0, .0, .0]

scale = 3
nb_segments = 3
rayon = 100
D = rayon * 2
c = D * math.pi
# segment = round(c / nb_segments, 6)
# segment = round((rayon + scale) * math.sin(math.radians(180 / nb_segments)), 6)
a = 360 / nb_segments
sx = 2 * rayon * math.sin(math.radians(a) / 2)
sy = 20
sz = 1

print(rayon, sx, sy, sz)

origin = (0., 0.)
point = (0., rayon )
print(origin, point)


def rotate(origin, point, angle):
    """
    Rotate a point counterclockwise by a given angle around a given origin.

    The angle should be given in radians.
    """
    ox, oy = origin
    px, py = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return qx, qy


def get_segments():
    polys = []

    polys.append({
        "n": "Cylinder",
        "p": [0, 0, 0],
        "r": [270, 0, 0],
        "s": [sx, sx, 1],
        "c": [1, 0, 0]
    })

    for x in range(nb_segments):
        angle = math.radians(a) * x

        # Origin
        ox = 0
        oy = 0
        oz = 0

        px = ox + math.cos(angle) * rayon
        py = ox + math.sin(angle) * rayon
        pz = sy / 2

        rotation = rotate(origin, point, _a)
        poly = {}
        poly["n"] = "Box"
        poly["p"] = [
            -round(rotation[0], 6),
            sy / 2,
            round(rotation[1], 6)
        ]
        poly["r"] = [.0, round(math.degrees(angle), 6), .0]
        # poly["s"] = [sx, sy, sz]
        poly["s"] = [sy, sy, sy]
        poly["c"] = [x / 10, x / 10, x / 10]

        polys.append(poly)

    return polys


def get_data():
    group = {
        "valuetype": "float",
        "objects": [
            {
                "n": "group",
                "objects": get_segments()
            }
        ]

    }
    return json.dumps(group, indent=2)


def write_file():
    fichier = open('test.world', 'w')
    fichier.write(get_data())
    fichier.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    write_file()

    # for x in range(6):
    #     result = rotate(origin, point, math.radians(360 / 6 *x))
    #     print(result)
