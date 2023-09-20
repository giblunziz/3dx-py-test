import math

from models.AbstractModel import AbstractModel


class Polygon(AbstractModel):

    def __init__(self, segments=8, radius=10):
        self.segments = segments
        self.radius = radius
        self.angle = math.radians(360 / self.segments)
        self.length = round(2 * math.sin(self.angle / 2) * self.radius, 6)

    def __get_segments(self):
        result = []

        for segment in range(self.segments):
            px = round(math.cos(self.angle * segment) * self.radius, 2)
            py = 0.
            pz = round(math.sin(self.angle * segment) * self.radius, 2)
            position = [px, py, pz]

            rx = 0.
            ry = round(math.degrees(self.angle * segment), 2)
            rz = 0.
            rotation = [rx, ry, rz]

            sx = round(self.length, 2)
            sy = 1.
            sz = 1.
            scale = [sx, sy, sz]

            color = [1., 0., .5]

            box = {
                "n": "Box",
                "p": position,
                "r": rotation,
                "s": scale,
                "c": color
            }
            result.append(box)
        return result

    def get_model(self):
        return self.poly()

    def poly(self, grouped=True):
        segments = self.__get_segments()
        if grouped:
            result = {
                "n": "group",
                "objects": segments
            }
        else:
            result = segments

        return result

    def dump(self):
        print(f"Segments: {self.segments}")
        print(f"radius: {self.radius}")
        print(f"angle: {self.angle}")
        print(f"length: {self.length}")
