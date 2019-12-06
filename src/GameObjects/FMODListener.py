import pygame
import pyfmodex
from pyfmodex.flags import MODE
from GameObjects.DraggableObject import DraggableObject
from FMODManagement.FMOD import FMOD

class FMODListener(DraggableObject):
    _listener = None

    def __init__(self):
        """
        Set source's sound, mode, creates a channel and plays it
        """
        super()
        self._listener = FMOD.createListener()
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
        FMOD.setListenerPosition(self._listener, position)


