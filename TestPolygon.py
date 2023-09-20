from models.Polygon import Polygon
from utils.World import World

if __name__ == '__main__':
    world = World(debug=True)
    world.append_model(Polygon(segments=8, radius=10))
    world.append_model(Polygon(segments=3, radius=5))

    w = world.get_world()
    world.save()
    # world.dump()
