import math

import numpy as np

from models.AbstractModel import AbstractModel


class Polygon(AbstractModel):

    def __init__(self, segments=8, radius=10):
        self.segments = segments
        self.radius = radius
        self.angle = math.radians(360 / self.segments)
        self.length = round(2 * math.sin(self.angle / 2) * self.radius, 6)

    def __get_median(self, p):

        # WIP
        # ab = np.array([a, b])
        # bc = np.array([b, c])
        # ca = np.array([c, a])
        #
        # amx = np.median(ab, axis=0)
        # amy = np.median(bc, axis=0)
        # amz = np.median(ca, axis=0)
        pass

    def __get_segments(self):

        for segment in range(self.segments):
            position = [
                round(math.cos(self.angle * segment) * self.radius, 2),
                0.,
                round(math.sin(self.angle * segment) * self.radius, 2)
            ]

            rotation = [0., round(math.degrees(self.angle * segment), 2), 0.]
            scale = [round(self.length, 2), 1., 1.]
            color = [1., 0., 0.]

            shape = np.array([position, rotation, scale, color])
            self.shapes.append(shape)

            # box = {"n": "Box", "p": position, "r": rotation, "s": scale, "c": color}
            # result.append(box)
        return self.as_world()

    def get_model(self):
        super().get_model()
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
