from os import listdir
from os.path import isdir
from pygame import image
from os.path import isfile, join

class ResourcesManager:
    _imageDictionary = {} #stores every image {key : image}

    def __init__(self):
        pass

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
        Get an image from the dictionary. If it des not exists, returns nothing and
        informs the user
        """
        if imageName in self._imageDictionary:
            return self._imageDictionary[imageName]
        else: 
            print(str(imageName) + " is not in the dictionary")
            
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
        files = [f for f in listdir(directoryPath) if isfile(join(directoryPath, f))]
        for filePath in files:
            self._imageDictionary[filePath] = image.load(self._formatPath(directoryPath, filePath))
            