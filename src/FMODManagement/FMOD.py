import pyfmodex
from pyfmodex.flags import MODE

class FMOD:
    _system = None #static variable

    @staticmethod
    def init():
        """
        inits the system from FMOD
        """
        if FMOD._system == None:
            FMOD._system = pyfmodex.System()
            FMOD._system.init()

    @staticmethod
    def release():
        if FMOD._system != None:
            FMOD._system.release()

    @staticmethod
    def loadSound(path):
        """
        Called by resources manager. Loads a sound and returns it
        """
        return FMOD._system.create_sound(path, False)

    @staticmethod
    def createChannel(sound, mode = MODE.DEFAULT):
        """
        creates a channel with the given sound and mode
        """
        channel = sound
        channel.mode = mode
        return channel

    @staticmethod
    def setChannelMode(channel, mode):
        """
        sets channel's mode
        """
        channel.mode = mode

    @staticmethod
    def playChannel(channel):
        """
        Plays a given channel
        """
        channel.play()