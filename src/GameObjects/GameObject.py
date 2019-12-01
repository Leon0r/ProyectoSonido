class GameObject:
    x, y, width, height = 0, 0, 50, 50
    active = True

    #@abstractmethod
    def render(self, pygameScreen):
        pass

    #@abstractmethod
    def update(self, time):
        pass

    #@abstractmethod
    def handleInput(self, event):
        pass

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def getPosition(self):
        """
        Returns tuple (x, y)
        """
        return (self.getX(), self.getY())

    def isActive(self):
        return self.active

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def setPosition(self, position):
        """
        Set the x and y of this game object.
        Position = tuple (x, ys)
        """
        self.setX(position[0])
        self.setY(position[1])

    def setWidth(self, width):
        self.width = width

    def setHeight(self, height):
        self.height = height

    def setActive(self, active):
        self.active = active
