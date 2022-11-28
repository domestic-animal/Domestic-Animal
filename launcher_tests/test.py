import unittest
import sys
import os
 
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from customization import Customization

class launcherTests(unittest.TestCase):
    def testControls(self):
        self.assertTrue(Customization.validateControls(['a','b','c','LSHIFT']))
        self.assertTrue(Customization.validateControls(['q']))
        self.assertFalse(Customization.validateControls(['LCTRL','LCTRL']))
        self.assertFalse(Customization.validateControls(['a','b','c','u','p','c']))
        

    
if __name__ == '__main__':
    unittest.main()