class AbstractModel:
    origin = [0, 0, 0]
    shapes = []
    shape_model = "Box"

    def get_model(self):
        self.shapes = []

    def as_world(self):
        model = []
        for shape in self.shapes:
            model.append(
                {
                    "n": self.shape_model,
                    "p": shape[0].tolist(),
                    "r": shape[1].tolist(),
                    "s": shape[2].tolist(),
                    "c": shape[3].tolist()
                }
            )
        return model
