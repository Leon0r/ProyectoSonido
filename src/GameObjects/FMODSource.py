import pygame
import pyfmodex
from pyfmodex.flags import MODE
from GameObjects.DraggableObject import DraggableObject
from FMODManagement.FMOD import FMOD

class FMODSource(DraggableObject):
    _sound = None
    _mode = None
    _channel = None

    def __init__(self, sound, mode = MODE.DEFAULT):
        """
        Set source's sound, mode, creates a channel and plays it
        """
        super()
        self._sound = sound
        self._mode = mode
        self._channel = FMOD.createChannel(self._sound, self._mode)
        self.setPosition(self.getPosition())

    def setSound(self, sound):
        """
        sets source's sound
        """
        self._sound = sound

    def setMode(self, mode):
        """
        sets source's mode (changes the channel mode itself)
        """
        self._mode = mode
        FMOD.setChannelMode(self._channel, self._mode)

    def setPosition(self, position):
        """
        redefined setPosotion. Sets the go position and the fmodsource's position
        """
        super().setPosition(position)
        FMOD.setChannelPosition(self._channel, self.getPosition())


