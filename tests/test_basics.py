import unittest
from phaseplot import phase_portrait
import matplotlib

class TestBasics(unittest.TestCase):
    """A collection of basic tests with no particular theme"""
    
    def test_retval(self):
        """phase_portrait returns an AxesImage instance"""
        def somefun(z): return z*z + 1
        retval = phase_portrait(somefun)
        self.assertIsInstance(retval, matplotlib.image.AxesImage)
