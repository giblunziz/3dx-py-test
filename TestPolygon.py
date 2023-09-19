from models.Polygon import Polygon
from utils.World import World

if __name__ == '__main__':
    world = World(debug=True)
    poly = Polygon(segments=8, radius=10)
    # poly.dump()
    s = poly.poly()
    world.append(s)

    w = world.get_world()
    world.save()
