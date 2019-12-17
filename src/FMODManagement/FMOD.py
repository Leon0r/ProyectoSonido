import pyfmodex
import FMODManagement.REVERB_PRESETS as reverb_presets
from pyfmodex.flags import MODE, TIMEUNIT
from pyfmodex.system import System, Listener, ThreedSettings
from pyfmodex.reverb import Reverb3D
from pyfmodex.structures import VECTOR
from pyfmodex.exceptions import FmodError
from pyfmodex.utils import ckresult
from pyfmodex.globalvars import dll as _dll
from ctypes import *

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
        """
        sets channel position. pos -> tuple (x, y)
        """
        channel.position = [pos[0], pos[1], 0]

    @staticmethod
    def createListener():
        """
        creates a fmod listener and returns it
        """
        return FMOD._system.listener(0)

    @staticmethod
    def setListenerPosition(listener, pos):
        """
        sets listener position. pos -> tuple (x, y)
        """
        listener.position = [pos[0], pos[1], 0]

    @staticmethod
    def setRollOffScale(scale):
        """
        Scale factor representation
        """
        FMOD._threedSettings.rolloff_scale = scale

    @staticmethod
    def createReverb(preset = reverb_presets.reverb_underwater, x = 0, y = 0, z = 0, min = 1, max = 1000):
        """
        create a reverb object. Redefined with Jaime's code
        """
        r = FMOD._system.create_reverb_3d()
        ckresult(_dll.FMOD_Reverb3D_SetActive(r._ptr, True))
        pos = VECTOR(x,y,z)

        # por alguna razon no coge directamente estos float y hay que enviarlos como c_float
        fmin = c_float(min)
        fmax = c_float(max)
        ckresult(_dll.FMOD_Reverb3D_Set3DAttributes(r._ptr, byref(pos), fmin, fmax))
        
        props = preset
        ckresult(_dll.FMOD_Reverb3D_SetProperties(r._ptr, byref(props)))
        return r

    @staticmethod
    def setReverbPosition(reverb, pos):
        """
        sets reverb position. pos -> tuple (x, y)
        """
        aux = [pos[0], pos[1], 0]
        reverb.position = aux
    
    @staticmethod
    def setReverbMinDistance(reverb, minDist):
        """
        sets a reverb's min distance of effect
        """
        reverb.min_distance = minDist

    @staticmethod
    def setReverbMaxDistance(reverb, maxDist):
        """
        sets a reverb's max distance of effect
        """
        reverb.max_distance = maxDist

    @staticmethod
    def createGeometry(maxpoligons = 1, maxvertices = 4):
        """
        creates a FMOD geometry object. In order for it to work, you need 
        to establish the polygons (FMOD doc, source: https://www.rubydoc.info/gems/fmod/FMOD/Geometry)
        """
        return FMOD._system.create_geometry(maxpoligons, maxvertices)

    @staticmethod
    def setGeometryPosition(geometry, pos):
        """
        sets geometry position. pos -> tuple (x, y)
        """
        geometry.position = [10.0, 10.0, 0.0]

    # @staticmethod
    # def addPolygonToGeometry(geometry, ...):
    #     addPolygon...
