import pyfmodex
from pyfmodex.flags import MODE, TIMEUNIT
from pyfmodex.system import System, Listener, ThreedSettings

class FMOD:
    _system = None #static variable
    _threedSettings = None

    @staticmethod
    def init():
        """
        inits the system from FMOD
        """
        if FMOD._system == None:
            FMOD._system = pyfmodex.System()
            FMOD._system.init()
            FMOD._threedSettings = FMOD._system.threed_settings

    @staticmethod
    def release():
        if FMOD._system != None:
            FMOD._system.release()

    @staticmethod
    def update():
        FMOD._system.update()

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
        return channel.play()

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

    @staticmethod
    def setChannelPosition(channel, pos):
        channel.position = [pos[0], pos[1], 0]

    @staticmethod
    def createListener():
        return FMOD._system.listener(0)

    @staticmethod
    def setListenerPosition(listener, pos):
        listener.position = [pos[0], pos[1], 0]

    @staticmethod
    def setRollOffScale(scale):
        """
        Scale factor representation
        """
        FMOD._threedSettings.rolloff_scale = scale

