import pygame
import pyfmodex
from GameObjects.DraggableObject import DraggableObject
from FMODManagement.FMOD import FMOD
from pyfmodex.structures import VECTOR
from ctypes import c_float, byref

class FMODGeometry(DraggableObject):
    """
    To create Geometry, once pressed the option in the menu, 
    use LEFT_CLICK to set vertexes on screen, 
    press RIGHT_CLICK when finished 
    """
    _geometry = None
    _isBeingCreated = True # true since creation till RIGHT_CLICK
    _vertexes = []
    _numVertex = 0 # amount of vertexes

    def __init__(self):
        """
        Creates a fmod geometry and sets its position to default (0, 0, 0)
        Changes the cursor and initializes the game object
        """
        super()
        self._geometry = FMOD.createGeometry()
        self.setPosition(self.getPosition())
        pygame.mouse.set_cursor(*pygame.cursors.broken_x) # changes cursor to mark geometry is being created


    def addGeometry(self):
        """
        Creates a fmod geometry and sets its position to default (0, 0, 0)
        """
        if self._numVertex > 1:
            numPolygon = self._numVertex-1
            self._geometry = FMOD.createGeometry(numPolygon + 1, (numPolygon + 2)* 4)
            self.setPosition((0,0))

            for v in range(numPolygon): # Loop through the number of polygons, creating them
                vert = (VECTOR(self._vertexes[v][0], self._vertexes[v][1], 1),
                        VECTOR(self._vertexes[v+1][0], self._vertexes[v+1][1], 1),
                        VECTOR(self._vertexes[v+1][0], self._vertexes[v+1][1], -1),
                        VECTOR(self._vertexes[v][0], self._vertexes[v][1], -1))

                FMOD.addPolygonsToGeometry(self._geometry, vert)



    def render(self, pygameScreen):
        """
        Renders the line that the polygons are going to follow
        Overrides parent render since it doesn't use sprite
        """

        if self._numVertex > 1:
            for v in range(self._numVertex - 1):
                pygame.draw.line(pygameScreen, 0xB13B9B, self._vertexes[v],self._vertexes[v+1], 3)

    def handleInput(self, event):
        """
        handle left click button to add vertex
        handle right click button to end geometry creation
        """
        handled = super().handleInput(event)
        if self.isActive():  # only if this is active
            if self._isBeingCreated:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # 1: LEFT_CLICK
                        mousePosition = pygame.mouse.get_pos()
                        self._vertexes.append(mousePosition)
                        self._numVertex += 1
                    elif event.button == 3:  # 3: RIGHT_CLICK
                        pygame.mouse.set_cursor(*pygame.cursors.arrow) # changes cursor to mark geometry is finished
                        self._isBeingCreated = False
                        self.addGeometry()

        return handled

    def setPosition(self, position):
        """
        redefined setPosition. Sets the go position and the fmodlistener position
        """
        super().setPosition(position)
        FMOD.setGeometryPosition(self._geometry, position)

    def release(self):
        """
        calls fmod release geometry
        """
        self._geometry.release()