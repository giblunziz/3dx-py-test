import numpy as np


class AbstractModel:
    origin = [0, 0, 0]
    shapes = []

    def get_model(self):
        self.shapes = []

    def as_world(self, name="Box"):
        model = []
        for shape in self.shapes:
            model.append(
                {
                    "n": name,
                    "p": shape[0].tolist(),
                    "r": shape[1].tolist(),
                    "s": shape[2].tolist(),
                    "c": shape[3].tolist()
                }
            )
        return model

    @staticmethod
    def medians(shapes):
        """
        Return the median of the 'position' part of the world object matrix (shape[,0])

        shapes: ndarray
            the original [[3,4]] dn array of shape with first line containing 'position' data

        returns: ndarray
            a copy of the shapes with the medians location of shapes [[a.b], [b.c], [c.n], [n.a]]
        """
        shapes_copy = shapes.copy()
        shapes_copy = np.append(shapes_copy, [shapes_copy[0]], 0)
        shapes = shapes.copy()

        for i in range(1, shapes_copy.shape[0]):
            shapes[i - 1, 0] = np.median([shapes_copy[i - 1, 0], shapes_copy[i, 0]], axis=0)
        return shapes
