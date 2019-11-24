class GameObject:
    x, y, width, height = 0, 0, 0, 0
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

    def isActive(self):
        return self.active

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def setWidth(self, width):
        self.width = width

    def setHeight(self, height):
        self.height = height

    def setActive(self, active):
        self.active = active
