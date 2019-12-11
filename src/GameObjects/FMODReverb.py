import pygame
import pyfmodex
from pyfmodex.flags import MODE
from GameObjects.DraggableObject import DraggableObject
from FMODManagement.FMOD import FMOD

class FMODReverb(DraggableObject):
    _reverb = None

    def __init__(self):
        """
        Set source's sound, mode, creates a channel and plays it
        """
        super()
        self._reverb = FMOD.createReverb()
        self.setMinDistance(0)
        self.setMaxDistance(100)
        self.setPosition(self.getPosition())

    def render(self, pygameScreen):
        """
        Renders the sprite at current (x, y) position
        """
        #maybe draw the cones --> ?? pygame.draw.polygon(pygameScreen, 0x00ff00, ((self.getX() + self.getWidth()/2, self.getY() + self.getHeight()/2), (self.getX() + self.getWidth()/2 - 50, self.getY() - 50), (self.getX() + self.getWidth()/2 + 50, self.getY() - 50)))
        super().render(pygameScreen)

    def update(self, time):
        super().update(time)

    def handleInput(self, event):
        """
        Handles dragging event
        """
        super().handleInput(event)

    def setPosition(self, position):
        super().setPosition(position)
        FMOD.setReverbPosition(self._reverb, position)

    def setMinDistance(self, minDist):
        FMOD.setReverbMinDistance(self._reverb, minDist)
    
    def setMaxDistance(self, maxDist):
        FMOD.setReverbMaxDistance(self._reverb, maxDist)
