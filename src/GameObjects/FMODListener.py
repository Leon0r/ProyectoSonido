import pygame
import pyfmodex
from pyfmodex.flags import MODE
from GameObjects.DraggableObject import DraggableObject
from FMODManagement.FMOD import FMOD

class FMODListener(DraggableObject):
    _listener = None

    def __init__(self):
        """
        Creates the listeners and set its position to default (0, 0)
        """
        super()
        self._listener = FMOD.createListener()
        self.setPosition(self.getPosition())

    def setPosition(self, position):
        """
        redefined setPosition. Sets the go position and the fmodlistener position
        """
        super().setPosition(position)
        FMOD.setListenerPosition(self._listener, position)


