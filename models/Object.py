import numpy as np


class Object:

    def __init__(self):
        self.position = np.array([0, 0, 0])
        self.rotation = np.array([0, 0, 0])
        self.scale = np.array([0, 0, 0])
        self.color = np.array([1, 1, 1])
