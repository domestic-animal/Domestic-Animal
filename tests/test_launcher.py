import sys
import pygame
sys.path.insert(0, './launcher')

from customization import Customization


def testControlsValidation():
    assert(Customization.validateControls({'up': 'U', 'down': 'P', 'left': 'S', 'right': 'D', 'fire': 'X'}) == True)
    assert(Customization.validateControls({'up': 'U', 'down': 'P', 'left': 'S', 'right': 'D', 'fire': 'D'}) == False)
    
    
    
def testControlsMapping():
    Input = {"up" : "", "down" : "","left" : "", "right" : "", "fire" : ""}
    
    expected = {"up" : pygame.K_UP, "down" : pygame.K_DOWN, 
                   "left" : pygame.K_LEFT, "right" : pygame.K_RIGHT, "fire" : pygame.K_SPACE}
    
    assert(Customization.mapControls(Input) == expected)
    
    Input = {"up" : "w", "down" : "s","left" : "a", "right" : "d", "fire" : "LCTRL"}
    
    expected = {"up" : pygame.K_w, "down" : pygame.K_s, 
                   "left" : pygame.K_a, "right" : pygame.K_d, "fire" : pygame.K_LCTRL}
    
    assert(Customization.mapControls(Input) == expected)

    