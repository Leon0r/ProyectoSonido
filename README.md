ProyectoSonido

In order to make pyfmodex work in windows, you need to modify the first lines of your fmodex.py to:

if arch == "32bit":
    _dll = CDLL(".\\x86\\core\\fmod.dll")
else:
    _dll = CDLL(".\\x64\\core\\fmod.dll")