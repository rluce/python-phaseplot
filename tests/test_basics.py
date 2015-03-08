import unittest
from phaseplot import phase_portrait
import matplotlib
from matplotlib import pyplot as plt

class TestBasics(unittest.TestCase):
    """A collection of basic tests with no particular theme"""
    
    def test_retval(self):
        """phase_portrait returns an AxesImage instance"""
        def somefun(z): return z*z + 1
        retval = phase_portrait(somefun)
        self.assertIsInstance(retval, matplotlib.image.AxesImage)


    def test_extent(self):
        """Test that the 'box' argument matches extent"""

        # See also: issue #1

        ai = phase_portrait(lambda(z) : z, box = (-1,1,-1,1))
        # extent = (left, right, bottom, top)
        extent = ai.get_extent()
        self.assertEqual( extent, (-1, 1, -1, 1) )

        ai = phase_portrait(lambda(z) : z, box = (-1,2,-3,4))
        # extent = (left, right, bottom, top)
        extent = ai.get_extent()
        self.assertEqual( extent, (-1, 2, -3, 4) )
