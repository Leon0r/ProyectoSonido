import pygame
import pyfmodex
from pyfmodex.flags import MODE
from GameObjects.DraggableObject import DraggableObject
from FMODManagement.FMOD import FMOD
from FMODManagement.REVERB_PRESETS import reverb_list, getReverbByIndex


class FMODReverb(DraggableObject):
    _reverb = None
    _reverbIndex = 0

    def __init__(self):
        """
        Set source's sound, mode, creates a channel and plays it
        """
        super()
        self._reverb = FMOD.createReverb()
        self.setMinDistance(1)
        self.setMaxDistance(1000)
        self.setPosition(self.getPosition())

    def handleInput(self, event):
        """
        Handles dragging event and right click reverb (changes the reverb, prints selected reverb)
        """
        handled = super().handleInput(event)
        if self.isActive():  # only if this is active
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:  # 3: RIGHT_CLICK
                    mousePosition = pygame.mouse.get_pos()
                    if self._hasClickedInside(mousePosition):
                        nReverb = getReverbByIndex(self._reverbIndex)
                        print("Current reverb: " + str(nReverb[1]))
                        FMOD.setReverbProperties(self._reverb, nReverb[0])
                        self._reverbIndex += 1
                        handled = True

        return handled

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

    def release(self):
        """
        deactivates the reverb and calls fmod reverb release
        """
        self._reverb.active = False
        FMOD.update()  # if you dont call system.update before releasing an object, all the changes made to it are not applied
        self._reverb.release()
        self._reverb = None
