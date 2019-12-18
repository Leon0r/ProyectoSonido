import pygame
from GameObjects.Sprite import Sprite
from GameObjects.GameObject import GameObject
from Utils.Utils import positionIsInsideRect

class DraggableObject(GameObject):
    """
    This object contains a sprite to render, methods to modify that sprite and
    the ability to be dragged around the screen by the user's input (mouse dependant).
    """
    _sprite = None
    _isBeingDragged = False
    _offsetX = 0 #offsetX with mousePosition
    _offsetY = 0 #offsetY with mousePosition

    def __init__(self):
        """
        Empty constructor
        """
        pass

    def render(self, pygameScreen):
        """
        Renders the sprite at current (x, y) position
        """
        #maybe draw the cones --> ?? pygame.draw.polygon(pygameScreen, 0x00ff00, ((self.getX() + self.getWidth()/2, self.getY() + self.getHeight()/2), (self.getX() + self.getWidth()/2 - 50, self.getY() - 50), (self.getX() + self.getWidth()/2 + 50, self.getY() - 50)))
        self._sprite.render(pygameScreen, self.getX(), self.getY())

    def handleInput(self, event):
        """
        Handles dragging event
        """
        handled = False
        if self.isActive(): #only if this is active
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: #3: LEFT_CLICK
                    mousePosition = pygame.mouse.get_pos()
                    self._isBeingDragged = self._hasClickedInside(mousePosition) and True #check if the user
                    #has clicked inside the game object
                    if self._isBeingDragged: #calculate the offset wit the mousePosition if this is being dragged
                        self._offsetX, self._offsetY = self._calculateOffset(mousePosition)
                        handled = True 
            elif event.type == pygame.MOUSEMOTION:
                self._moveGameObject(pygame.mouse.get_pos()) 
                handled = True
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1: #3: LEFT_CLICK
                    self._isBeingDragged = False #the user has stopeed dragging this gameObject
                    handled = True
        return handled

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
        super(DraggableObject, self).setWidth(width)
        self._sprite.setSize(self.getWidth(), self.getHeight())

    def setHeight(self, height):
        """
        Parent's method redefinition. Calls super.setHeight
        and resets sprite's size to the new height. WARNING: IF YOU SET
        HEIGHT TO 0, THE SPRITE CANNOT BE SEEN AGAIN (PYGAME THINGS).
        """
        super(DraggableObject, self).setHeight(height)
        self._sprite.setSize(self.getWidth(), self.getHeight())

    def _hasClickedInside(self, mousePosition):
        """
        checks if the user has clicked inside the rectangle of this gameObject
        """
        return positionIsInsideRect(mousePosition, 
            (self.getX(), self.getY(), self.getWidth(), self.getHeight()))

    def _moveGameObject(self, mousePosition):
        """
        moves the game object is its being dragged, according to the offset calculated before
        """
        if self._isBeingDragged:
            self.setPosition(self._getOffsetPosition(mousePosition))

    def _getOffsetPosition(self, position):
        """
        simple offset with a position
        """
        return (position[0] + self._offsetX, position[1] + self._offsetY)

    def _calculateOffset(self, mousePosition):
        """
        calculates the offset regarding the mouse position
        """
        return self.getX() - mousePosition[0], self.getY() - mousePosition[1]

