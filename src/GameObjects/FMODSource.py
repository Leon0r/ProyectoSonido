import pygame
import pyfmodex
from pyfmodex.flags import MODE
from GameObjects.DraggableObject import DraggableObject
from FMODManagement.FMOD import FMOD
from Utils.ResourcesManager import ResourcesManager

class FMODSource(DraggableObject):
    _sound = None
    _mode = None

    def __init__(self, sound, mode = MODE.DEFAULT):
        """
        Set source's sound, mode, creates a channel and plays it
        """
        super()
        self._sound = sound
        self._mode = mode
        FMOD.createChannel(self._sound, self._mode)
        FMOD.playChannel(sound)

    def render(self, pygameScreen):
        """
        Renders the sprite at current (x, y) position
        """
        super().render(pygameScreen)

    def update(self, time):
        super().update(time)

    def handleInput(self, event):
        """
        Handles dragging event
        """
        super().handleInput(event)

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
        FMOD.setChannelMode(self._mode)


