from typing import MutableSequence
import pygame.mixer as mix

class Music():

    def __init__(self, music: MutableSequence[str]):
        self.music = music  # Array of the music absolutePaths
        self.track = 0      # the current played track
        self.paused = False # Pause indicator

    def loadTrack(self, track = 0):
        mix.music.unload()
        mix.music.load(self.music[track])

    def play(self):
        mix.music.play(-1)

    def pauseToggle(self):
        if not self.paused:
            mix.music.pause()
        else:
            mix.music.unpause()
        self.paused = not self.paused
    
    def stop():
        mix.music.stop()

    # def pause(self):
    #     if not self.paused:
    #         mix.music.pause()
    #     self.paused = True
    
    # def resume(self):
    #     if self.paused:
    #         mix.music.unpause()
    #     self.paused = False
