from pygame import display
from pygame.transform import scale


class Sprite:
    _image = None

    def __init__(self, image=None):
        """
        Initializes sprite with the given image
        """
        self._image = image

    def render(self, pygameScreen, x, y):
        """
        Renders the image at (x, y) position in pygameScreen
        """
        pygameScreen.blit(self._image, (x, y))

    def setSize(self, width, height):
        """
        Sets the size of the current image
        """
        self._image = scale(self._image, (width, height))

    def setImage(self, image):
        """
        Sets sprite's image
        """
        self._image = image
