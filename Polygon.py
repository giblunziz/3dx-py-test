import math


class Polygon:

    def __init__(self, segments=8, radius=10):
        self.segments = segments
        self.radius = radius
        self.angle = math.radians(360 / self.segments)
        self.length = round(2 * math.sin(self.angle / 2) * self.radius, 6)

    def test(self):
        for segment in range(self.segments):
            px = round(math.cos(self.angle * segment) * self.radius, 2)
            py = round(math.sin(self.angle * segment) * self.radius, 2)
            pz = 0.
            P = [px, py, pz]

            rx = 0.
            ry = round(math.degrees(self.angle * segment), 2)
            rz = 0.
            R = [rx, ry, rz]

            sx = 1.
            sy = round(self.length, 2)
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
            print(f"Box {segment}: {box}")

    def dump(self):
        print(f"Segments: {self.segments}")
        print(f"radius: {self.radius}")
        print(f"angle: {self.angle}")
        print(f"length: {self.length}")
