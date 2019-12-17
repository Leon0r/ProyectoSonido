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
        self.setMinDistance(1)
        self.setMaxDistance(1000)
        self.setPosition(self.getPosition())

    def render(self, pygameScreen):
        """
        Renders the sprite at current (x, y) position
        """
        #maybe draw the cones --> ?? pygame.draw.polygon(pygameScreen, 0x00ff00, ((self.getX() + self.getWidth()/2, self.getY() + self.getHeight()/2), (self.getX() + self.getWidth()/2 - 50, self.getY() - 50), (self.getX() + self.getWidth()/2 + 50, self.getY() - 50)))
        super().render(pygameScreen)

    def update(self, time):
        """
        update of the gameObject
        """
        super().update(time)

    def handleInput(self, event):
        """
        Handles dragging event
        """
        return super().handleInput(event)

    def setPosition(self, position):
        """
        redefined setPositions. Sets the go position and the reverb position
        """
        super().setPosition(position)
        FMOD.setReverbPosition(self._reverb, position)

    def setMinDistance(self, minDist):
        """
        min dist of the reverb
        """
        FMOD.setReverbMinDistance(self._reverb, minDist)
    
    def setMaxDistance(self, maxDist):
        """
        max distance of the reverb
        """
        FMOD.setReverbMaxDistance(self._reverb, maxDist)
