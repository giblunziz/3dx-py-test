class Vehicule:

    def __init__(self):
        self.carburant = 5

    @classmethod
    def klaxonner(cls):
        print("Pouet")

    def rouler(self):
        if (self.carburant > 0):
            self.carburant -= 1
            print("Vroom")
            if (self.carburant == 0):
                print("ATTENTION, PLUS DE CARBURANT")
        else:
            print("Faite le plein!")


v = Vehicule()
Vehicule.klaxonner()

for i in range(10):
    v.rouler()
