import json


class World:
    __objects = []

    def __init__(self, debug=False):
        self.__debug = debug

    def get_world(self):
        group = {
            "valuetype": "float",
            "objects": self.__objects
        }
        return group

    def append(self, fragment):
        self.__objects.append(fragment)

    def save(self, filename='output/test.world'):
        fichier = open(filename, 'w')
        fichier.write(self.__as_json())
        fichier.close()

        if self.__debug:
            fichier = open(filename + ".json", 'w')
            fichier.write(self.__as_json())
            fichier.close()

    def dump(self):
        print(self.__as_json())

    def __as_json(self):
        return json.dumps(self.get_world(), indent=2)
