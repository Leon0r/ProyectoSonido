from GameObjects.Sprite import Sprite
from GameObjects.GameObject import GameObject
from pygame import display

class FMODObject(GameObject):
    _sprite = None

    def __init__(self):
        """
        Empty constructor
        """
        pass

    def setSpriteFromImage(self, image):
        """
        creates a new sprite and attaches it to this object. Set its size
        to the current wodth and height.
        """
        self._sprite = Sprite()
        self._sprite.setImage(image)
        self._sprite.setSize(self.getWidth(), self.getHeight())

    def setWidth(self, width):
        """
        Parent's method redefinition. Calls super.setWidth
        and resets sprite's size to the new width. WARNING: IF YOU SET
        WIDTH TO 0, THE SPRITE CANNOT BE SEEN AGAIN (PYGAME THINGS).
        """
        super(FMODObject, self).setWidth(width)
        self._sprite.setSize(self.getWidth(), self.getHeight())

    def setHeight(self, height):
        """
        Parent's method redefinition. Calls super.setHeight
        and resets sprite's size to the new height. WARNING: IF YOU SET
        HEIGHT TO 0, THE SPRITE CANNOT BE SEEN AGAIN (PYGAME THINGS).
        """
        super(FMODObject, self).setHeight(height)
        self._sprite.setSize(self.getWidth(), self.getHeight())

    def render(self, pygameScreen):
        """
        Renders the sprite at current (x, y) position
        """
        self._sprite.render(pygameScreen, self.getX(), self.getY())
