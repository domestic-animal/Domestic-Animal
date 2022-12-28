from typing import MutableSequence
import random
import pygame
pygame.init()
pygame.mixer.init()

class Music():
    """
    Music class handles playing, pausing & stoping the in-game background music
    """

    def __init__(self, music: MutableSequence[str]):
        self.music = music  # Array of the music absolutePaths
        self.track = 0      # the current played track
        self.paused = False # Pause indicator

    def loadTrack(self, track = 0):
        """
        Loads the wanted track into the pygame.pygame.mixerer.music
        
        :param track: the wanted track to play (-1 for random track)
        """
        pygame.mixer.music.unload()
        self.track = track
        if track == -1: #random track
            self.track = random.randint(0, len(self.music) - 1)
        pygame.mixer.music.load(self.music[self.track])

    def play(self):
        pygame.mixer.music.play(-1)

    def pauseToggle(self):
        if not self.paused:
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()
        self.paused = not self.paused
    
    def stop(self):
        pygame.mixer.music.stop()