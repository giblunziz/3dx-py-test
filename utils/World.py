import json
import logging

from models.AbstractModel import AbstractModel


class World:
    __models = []

    def __init__(self, debug=False):
        self.__debug = debug

    def get_world(self):
        group = {
            "valuetype": "float",
            "objects": self.get_model()
        }
        return group

    def append_model(self, model: AbstractModel):
        self.__models.append(model)

    def get_model(self):
        r = []
        for model in self.__models:
            r.append(model.get_model())
        return r

    def save(self, filename='output/test.world'):
        fichier = open(filename, 'w')
        fichier.write(json.dumps(self.get_world(), separators=(',', ':')))
        fichier.close()

        if self.__debug:
            fichier = open(filename + ".json", 'w')
            fichier.write(json.dumps(self.get_world(), indent=2))
            fichier.close()

    def dump(self):
        logging.info(self.__pretty())

    def __pretty(self):
        return json.dumps(self.get_world(), indent=2)
