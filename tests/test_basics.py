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

    def test_box_argument(self):
        """Test various ways to specify a plot box"""

        from numpy import sin

        # Method 1: Explicitly specify bounds for real(z) and imag(z)
        box = (-2,2,-2,2)
        ai = phase_portrait(sin, box=box)
        self.assertEqual(ai.get_extent(), box)

        # Method 2: Midpoint, re-part-radius, im-part-radius (infinity norm)
        box = (0, 3, 2)
        fullbox = (-3, 3, -2, 2)
        ai = phase_portrait(sin, box=box)
        self.assertEqual(ai.get_extent(), fullbox)

        # Method 3: lower-left corner & upper-right corner
        box = (-1-1j, 1+1j)
        fullbox = (-1,1,-1,1)
        ai = phase_portrait(sin, box=box)
        self.assertEqual(ai.get_extent(), fullbox)

        # Method 4: midpoint & real radius (infinity norm)
        box = (2 + 2j, 2)
        fullbox = (0, 4, 0, 4)
        ai = phase_portrait(sin, box=box)
        self.assertEqual(ai.get_extent(), fullbox)

        # Method 5: midpoint only (assumes radius == 1.0)
        box = (-1-1j)
        fullbox = (-2, 0, -2, 0)
        ai = phase_portrait(sin, box=box)
        self.assertEqual(ai.get_extent(), fullbox)


