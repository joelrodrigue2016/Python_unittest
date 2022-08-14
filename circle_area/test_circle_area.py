from math import *
from circle_area import *
import unittest

class Test_circle_area(unittest.TestCase):
    def test_area(self):
        #Test areas when radius >=0
        self.assertAlmostEqual(circle_area(1),pi)
        self.assertAlmostEqual(circle_area(0),0)
        self.assertAlmostEqual(circle_area(2.1),pi*2.1**2)
        self.assertAlmostEqual(circle_area(10),pi*10**2)
	
    def test_values(self):
         #test for values that are not integer        
        self.assertRaises(ValueError,circle_area,-2)

    def test_types(self):
        self.assertRaises(TypeError,circle_area,3+5j)
        self.assertRaises(TypeError,circle_area,True)
        self.assertRaises(TypeError,circle_area,"Joel")
        

        
        
 