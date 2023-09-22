import numpy as np
from mayavi import mlab


class Dataviz:

    def __init__(self):
        pass

    def draw(self, shapes):

        # x, y, z = np.mgrid[-5:5:50j, -5:5:50j, -5:5:50j]
        # scalar = np.sin(np.sqrt(x ** 2 + y ** 2 + z ** 2))
        fig = mlab.figure()
        # contour = mlab.contour3d(x, y, z, scalar, colormap='magma')

        print(shapes)
        for shape in shapes:
            print(type(shape))
            for kg, vg in shape.items():
                print(kg, vg)
                if kg == 'objects':
                    for sshape in vg:
                        print("sshape", sshape)
                        for ks, vs in sshape.items():
                            print("sshape key", ks, vs)
                            point = None
                            glyph = None
                            if ks == 'p':
                                point = mlab.points3d(vs[0], vs[1], vs[2], mode='cube')
                                glyph = point.glyph.glyph_source
                                glyph.glyph_source = point.glyph.glyph_source.glyph_dict['cube_source']
                                # print(dir(glyph._trfm.transform))

                                # glyph._trfm.transform.x_length(vs[0])
                                # glyph._trfm.transform.y_length(vs[1])
                                # glyph._trfm.transform.z_length(vs[2])
                            if ks == 'r' and glyph:
                                glyph._trfm.transform.rotate_x(vs[0])
                                glyph._trfm.transform.rotate_y(vs[1])
                                glyph._trfm.transform.rotate_z(vs[2])
                                print("glyph", glyph)

        mlab.xlabel('X')
        mlab.ylabel('Y')
        mlab.zlabel('Z')
        mlab.title('World Plot')
        mlab.show()
