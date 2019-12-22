import pygame
import pyfmodex
from pyfmodex.flags import MODE
from GameObjects.DraggableObject import DraggableObject
from Utils.ResourcesManager import ResourcesManager
from FMODManagement.FMOD import FMOD

class FMODSource(DraggableObject):
    _sound = None
    _mode = None
    _channel = None
    _soundIndex = 0

    def __init__(self, sound, mode = MODE.DEFAULT):
        """
        Set source's sound, mode, creates a channel and plays it
        """
        super()
        self._sound = sound
        self._mode = mode
        self._channel = FMOD.createChannel(self._sound, self._mode)
        self.setPosition(self.getPosition())

    def handleInput(self, event):
        """
        handle right click button over source (change the sound file)
        """
        handled = super().handleInput(event)
        if self.isActive(): #only if this is active
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3: #3: RIGHT_CLICK
                    mousePosition = pygame.mouse.get_pos()
                    if self._hasClickedInside(mousePosition):
                        self._soundIndex += 1
                        self.setSound(ResourcesManager.getInstance().getSoundByIndex(self._soundIndex))
                        handled = True
        return handled

    def setSound(self, sound):
        """
        sets source's sound
        """
        FMOD.stopChannel(self._channel)
        self._sound = sound
        self._channel = FMOD.createChannel(self._sound, self._mode)

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

    def release(self):
        """
        stops the channel and set it to none
        """
        super().release()
        FMOD.stopChannel(self._channel)
        self._channel = None


