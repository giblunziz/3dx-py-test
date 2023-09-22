import logging

from models.Polygon import Polygon
from utils.World import World

logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    world = World(debug=True)
    world.append_model(Polygon(segments=3, radius=50))
    # world.append_model(Polygon(segments=3, radius=5))

    # w = world.get_world()
    world.save()
    world.dump()

    world.draw()
    
