import pygame

def positionIsInsideRect(posToCheck, rect):
    """
    Check if a position is inside a given rectangle.
    posToCheck: position that is going to be checked
    rect: tuple. (left, top, width, height)
    """
    rect = pygame.Rect(rect[0], rect[1], rect[2], rect[3])
    return rect.collidepoint(posToCheck)
