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
        FMOD.setRollOffScale(0.01)

    def setPosition(self, position):
        """
        redefined setPosition. Sets the go position and the fmodlistener position
        """
        super().setPosition(position)
        FMOD.setListenerPosition(self._listener, position)

    def release(self):
        """
        sends away the listener (cant remove, cant deceease to 0 for some reason). Sets listener to None
        """
        super().release()
        self.setPosition((-5000, -5000))
        self._listener = None
