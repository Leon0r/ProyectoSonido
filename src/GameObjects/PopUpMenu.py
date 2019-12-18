import pygame
from GameObjects.GameObject import GameObject
from Utils.Utils import positionIsInsideRect

class MenuOption(GameObject):
    _name = "" #option name
    _font = None #font object. Creates the text surface
    _textSurface = None
    _mouseOver = False
    _callback = None #called in _executeButtonTask
    _args = None #callback's args

    def __init__(self, name, width, height, font, callback):
        """
        Option init. Sets name, font, width, height, callback, parameters
        and creates the text surface (needed to render text)
        """
        self._name = name
        self._font = font
        self.setWidth(width)
        self.setHeight(height)
        self._textSurface = self._font.render(self._name, False, (0, 0, 0))
        self._callback = callback[0]
        self._args = callback[1]

    def render(self, pygameScreen):
        """
        Renders option text and higlights it if _mouseOver equals true
        """
        if self.isActive():
            if self._mouseOver:
                pygame.draw.rect(pygameScreen, 0xd7c5f8, (self.getX(), self.getY(), self.getWidth(), self.getHeight()))

            pygameScreen.blit(self._textSurface, (self.getX(), self.getY()))

    def update(self, time):
        return

    def handleInput(self, event):
        """
        Checks if the mouse cursor is over the option and if the user
        left-clicked the button (todo: callback here)
        """
        handled = False
        if event.type == pygame.MOUSEMOTION:
            self._mouseOver = positionIsInsideRect(pygame.mouse.get_pos(), (self.getX(),
                self.getY(), self.getWidth(), self.getHeight())) #if the mouse
                #is over the option, its gonna be highlighted
            handled = self._mouseOver
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: #0: LEFT_CLICK
                handled = self._executeButtonTask()
        return handled

    def _executeButtonTask(self):
        """
        Executes the callback if the mouse is inside the button, returns true to indicate if this go has been handled
        """
        if positionIsInsideRect(pygame.mouse.get_pos(), (self.getX(),
            self.getY(), self.getWidth(), self.getHeight())):
            self._callback(*self._args)
            return True

        return False

class PopUpMenu(GameObject):
    _OPTION_HEIGHT = 50
    _color = 0xccedf3
    _menu_options = []
    _menu_font = None

    def __init__(self, optionsNames, callbacks, color):
        """
        Init menu's size (options length dependant), color, menu's font.
        Starts inactive. Creates the menu options with the given name and the
        given callback --> (foo, *args). Adds to callback args this object
        """
        self._menu_font = pygame.font.SysFont('Sylfaen', 35)
        self.setWidth(250)
        optionsNames = PopUpMenu._parseOptionsName(optionsNames)
        for i in range(len(optionsNames)):
            callbacks[i][1].append(self) #appends the object to the callback
            #parameters to get access to this object variables (needed for fmod maybe?)
            option = MenuOption(optionsNames[i], self.getWidth(),
                self._OPTION_HEIGHT, self._menu_font, callbacks[i])
            option.setActive(False)

            self._menu_options.append(option)

        self.setHeight(self._OPTION_HEIGHT * len(self._menu_options))
        self._color = color
        self.setActive(False)

    def render(self, pygameScreen):
        """
        Draw rectangle (color, x, y, width, height) and the options
        """
        if self.isActive():
            pygame.draw.rect(pygameScreen, self._color, (self.x, self.y, self.width, self.height))
            for option in self._menu_options:
                option.render(pygameScreen)

    def update(self, time):
        for option in self._menu_options:
            option.update(time)

    def handleInput(self, event):
        """
        Handles all user input involving the pop up menu (right click, left click,
        right clock inside an option)
        """
        handled = False
        if self.isActive(): #only if this is active -> send event to the options
            for option in self._menu_options:
                option.handleInput(event)

        #menu handler (hides and shows the menu)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3: #3: RIGHT_CLICK
                self.popMenu(pygame.mouse.get_pos())
                handled = True
            elif event.button == 1: #0: LEFT_CLICK
                self.hideMenu()
                handled = True
        return handled

    def popMenu(self, mousePos):
        """
        Sets the x, y of the menu and activates it
        """
        self.setX(mousePos[0])
        self.setY(mousePos[1])
        self.setActive(True)

        self._arrangeOptions()

    def hideMenu(self):
        """
        Sends away the menu and hides it
        """
        self.setX(-50000)
        self.setY(-50000)
        self.setActive(False)

        self._arrangeOptions()

    def _arrangeOptions(self):
        """
        Re-arrange the options depending on the position of the "parent" rectangle
        """
        for i in range(len(self._menu_options)):
            self._menu_options[i].setX(self.getX())
            self._menu_options[i].setY(self.getY() + (self._OPTION_HEIGHT * i))
            self._menu_options[i].setActive(self.isActive())

    @staticmethod
    def _parseOptionsName(names):
        """
        Parse the names of the options to nicely fit in the pop up menu
        """
        for i in range(len(names)):
            names[i] = " " + names[i]
        return names
