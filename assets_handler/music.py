from typing import MutableSequence
import pygame.mixer as mix
import random

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
        Loads the wanted track into the pygame.mixer.music
        
        :param track: the wanted track to play (-1 for random track)
        """
        mix.music.unload()
        self.track = track
        if track == -1: #random track
            self.track = random.randint(0, len(self.music) - 1)
        mix.music.load(self.music[self.track])

    def play(self):
        mix.music.play(-1)

    def pauseToggle(self):
        if not self.paused:
            mix.music.pause()
        else:
            mix.music.unpause()
        self.paused = not self.paused
    
    def stop(self):
        mix.music.stop()