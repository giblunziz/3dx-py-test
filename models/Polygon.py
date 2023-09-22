import logging
import math

import numpy as np

from models.AbstractModel import AbstractModel


class Polygon(AbstractModel):

    def __init__(self, segments=8, radius=10):
        self.segments = segments
        self.radius = radius
        self.angle = math.radians(360 / self.segments)
        self.length = round(2 * math.sin(self.angle / 2) * self.radius, 6)

    def __get_segments(self):
        l_shapes = []
        for segment in range(self.segments):
            position = np.array([
                round(math.cos(self.angle * segment) * self.radius, 2),
                0.,
                round(math.sin(self.angle * segment) * self.radius, 2)
            ])

            rotation = np.array([0., round(math.degrees(self.angle * segment), 2), 0.])
            scale = np.array([round(self.length, 2), 1., 1.])
            color = np.array([1., 1., 1.])

            shape = np.array([position, rotation, scale, color])
            l_shapes.append(shape)

            # box = {"n": "Box", "p": position, "r": rotation, "s": scale, "c": color}
            # result.append(box)
        self.shapes = self.medians(np.array(l_shapes))
        logging.debug("self.shapes: %s", self.shapes)
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
        logging.info(f"Segments: {self.segments}")
        logging.info(f"radius: {self.radius}")
        logging.info(f"angle: {self.angle}")
        logging.info(f"length: {self.length}")
