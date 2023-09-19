import json


class World:
    __objects = []

    def __init__(self):
        pass

    def get_world(self):
        group = {
            "valuetype": "float",
            "objects": self.__objects
        }
        return group

    def append(self, object):
        self.__objects.append(object)

    def save(self, filename='output/test.world'):
        fichier = open(filename, 'w')
        fichier.write(self.__as_json())
        fichier.close()

    def dump(self):
        print(self.__as_json())

    def __as_json(self):
        return json.dumps(self.get_world(), indent=2)
