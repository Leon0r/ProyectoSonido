# PYGAME / FMOD INTERFACE

PYGAME / FMOD INTERFACE is a Python program for showing FMOD functions.

## Installation

Download the repository, install pygame and pyfmodez (pip insyall). In Windows, change your fmodex.py file lines to:

```
if arch == "32bit":
    _dll = CDLL(".\\x86\\core\\fmod.dll") #this folders are provided with the repository
else:
    _dll = CDLL(".\\x64\\core\\fmod.dll")
```

```bash
pip install foobar
```

## Documentation

Folder "doc". Files diagram and html (index.html)
 
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.