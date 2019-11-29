import pygame
import sys
from GameObjects.PopUpMenu import PopUpMenu
from Utils.ResourcesManager import ResourcesManager
from Utils.Sprite import Sprite
from Utils.Utils import getStringCurrentWorkingDirectory

#--------------------------CALLBACK TEST------------
def callBackTest(f, a, _object):
    print(str(_object.getX()) + f + str(a)) #example of getting variable
    #parameters of an object

def callBackTest1(_object):
    print("Test1")

#-------------------PYGAME-------------------------
screen = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()
pygame.display.set_caption("Hello World")
pygame.font.init()
x = 0
#-------------------RESOURCES----------------------
resourcesManager = ResourcesManager()
resourcesManager.loadImagesFromDirectory(getStringCurrentWorkingDirectory() + "\\resources\\sprites")
spriteTest = Sprite(resourcesManager.getImage("ear.png"))
spriteTest.setSize(50, 50)
#-------------------GAME OBJECTS-------------------------
gameObjects = []
popUp = PopUpMenu(["holaa", "kk"], [(callBackTest, ["parameter", x]), (callBackTest1, [])], 0xaaaaaa)
gameObjects.append(popUp)
running = True
lastFrameTime = pygame.time.get_ticks()

while running:
    #clear
    screen.fill(0xff0000)
    #get events
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
            break

        for gameObject in gameObjects:
            gameObject.handleInput(e)

    currentTime = pygame.time.get_ticks()
    # deltaTime in seconds.
    deltaTime = (currentTime - lastFrameTime) / 1000.0
    #update
    for gameObject in gameObjects:
        gameObject.update(deltaTime)


    #render
    for gameObject in gameObjects:
        gameObject.render(screen)
    
    spriteTest.render(screen, 100, 100)

    #dumps data into the screen
    lastFrameTime = currentTime
    pygame.display.update()
    clock.tick(30)

pygame.display.quit()
pygame.quit()
sys.exit()
