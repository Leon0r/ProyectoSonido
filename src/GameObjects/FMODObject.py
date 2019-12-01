import pygame
from GameObjects.DraggableObject import DraggableObject

class FMODObject(DraggableObject):

    def __init__(self):
        """
        Empty constructor
        """
        super()

    def render(self, pygameScreen):
        """
        Renders the sprite at current (x, y) position
        """
        super().render(pygameScreen)

    def update(self, time):
        super().update(time)

    def handleInput(self, event):
        """
        Handles dragging event
        """
        super().handleInput(event)

