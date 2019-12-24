from os import listdir
from os.path import isdir
from pygame import image
from os.path import isfile, join
from FMODManagement import FMOD


class ResourcesManager:
    """
    Creates a dictionary for the images / sounds stored in the corresponding folders
    """
    _imageDictionary = {}  # stores every image {key : image}
    _soundsDictionary = {}
    _instance = None

    def __init__(self):
        pass

    @staticmethod
    def getInstance():
        """
        singleton pattern
        """
        if not ResourcesManager._instance:
            ResourcesManager._instance = ResourcesManager()

        return ResourcesManager._instance

    def loadImagesFromDirectory(self, directoryPath):
        """
        Check if the directory exists. If it exists, gets every image
        from it and stores them in a dictionary.
        """
        if isdir(directoryPath):
            self._getImagesFromDirectory(directoryPath)
        else:
            print(directoryPath + " does not exists")

    def getImage(self, imageName):
        """
        Get an image from the dictionary. If it does not exists, returns nothing and
        informs the user
        """
        if imageName in self._imageDictionary:
            return self._imageDictionary[imageName]
        else:
            print(str(imageName) + " is not in the dictionary")

    def loadSoundsFromDirectory(self, directoryPath):
        """
        Check if the directory exists. If it exists, gets every sound
        from it and stores them in a dictionary.
        """
        if isdir(directoryPath):
            self._getSoundsFromDirectory(directoryPath)
        else:
            print(directoryPath + " does not exists")

    def getSound(self, soundName):
        """
        Get a sound from the dictionary. If it does not exists, returns nothing and
        informs the user
        """
        if soundName in self._soundsDictionary:
            return self._soundsDictionary[soundName]
        else:
            print(str(soundName) + " is not in the dictionary")

    def getSoundByIndex(self, index):
        """
        Get a sound from the dictionary by the given index. (index % dic.length)
        """
        value = index % len(self._soundsDictionary)
        return list(self._soundsDictionary.values())[value]

    def release(self):
        """
        release all fmod sounds
        """
        for key in self._soundsDictionary.keys():
            self._soundsDictionary[key].release()

    @staticmethod
    def _formatPath(directoryPath, filePath):
        """
        Simple path formatter. Adds "\\" to the path
        """
        return directoryPath + "\\" + filePath

    def _getImagesFromDirectory(self, directoryPath):
        """
        Iterates through the images of directoryPath and loads them
        """
        files = [f for f in listdir(directoryPath)
                 if isfile(join(directoryPath, f))]
        for filePath in files:
            self._imageDictionary[filePath] = image.load(
                self._formatPath(directoryPath, filePath))

    def _getSoundsFromDirectory(self, directoryPath):
        """
        Iterates through the sounds of directoryPath and loads them
        """
        files = [f for f in listdir(directoryPath)
                 if isfile(join(directoryPath, f))]
        for filePath in files:
            self._soundsDictionary[filePath] = FMOD.FMOD.loadSound(
                self._formatPath(directoryPath, filePath))
