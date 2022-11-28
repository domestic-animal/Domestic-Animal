import unittest
import sys
import os
 
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from customization import Customization

class launcherTests(unittest.TestCase):
    def testControls(self):
        self.assertTrue(Customization.validateControls({'up': 'U', 'down': 'P', 'left': 'S', 'right': 'D', 'fire': 'X'}))
        self.assertFalse(Customization.validateControls({'up': 'U', 'down': 'P', 'left': 'S', 'right': 'D', 'fire': 'D'}))
        

    
if __name__ == '__main__':
    unittest.main()