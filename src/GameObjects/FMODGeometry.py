import pygame
import pyfmodex
from GameObjects.DraggableObject import DraggableObject
from FMODManagement.FMOD import FMOD

class FMODGeometry(DraggableObject):
    _geometry = None

    def __init__(self):
        """
        Creates a fmod geometry and sets its position to default (0, 0, 0)
        """
        super()
        self._geometry = FMOD.createGeometry()
        self.setPosition(self.getPosition())

    def setPosition(self, position):
        """
        redefined setPosition. Sets the go position and the fmodlistener position
        """
        super().setPosition(position)
        FMOD.setGeometryPosition(self._geometry, position)

    def release(self):
        """
        calls fmod release geometry
        """
        self._geometry.release()


