import sys
import pygame
from GameObjects.PopUpMenu import PopUpMenu
from GameObjects.FMODSource import FMODSource
from Utils.ResourcesManager import ResourcesManager
from Utils.Utils import getStringCurrentWorkingDirectory
from FMODManagement.FMOD import FMOD
from pyfmodex.flags import MODE

#--------------------------CALLBACKS------------
def callBackTest(f, a, _object):
    print(str(_object.getX()) + f + str(a)) #example of getting variable
    #parameters of an object

def addFMODSource(gameObjects, imageName, soundName, _object):
    fmodSource= FMODSource(resourcesManager.getSound(soundName), MODE.LOOP_NORMAL)
    fmodSource.setSpriteFromImage(resourcesManager.getImage(imageName))
    fmodSource.setX(_object.getX())
    fmodSource.setY(_object.getY())
    gameObjects.insert(0, fmodSource) #inserts the element at tht beggining of the list

#-------------------PYGAME-------------------------
screen = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()
pygame.display.set_caption("Hello World")
pygame.font.init()
x = 0

#-------------------FMOD--------------------------
FMOD.init()

#-------------------RESOURCES----------------------
resourcesManager = ResourcesManager()
resourcesManager.loadImagesFromDirectory(getStringCurrentWorkingDirectory() + "\\resources\\sprites")
resourcesManager.loadSoundsFromDirectory(getStringCurrentWorkingDirectory() + "\\resources\\sounds")

#-------------------GAME OBJECTS-------------------------
gameObjects = []
popUp = PopUpMenu(["Add Listener", "Add Source"], [(addFMODSource, [gameObjects, "ear.png", "0879_on_Exh.ogg"]), 
    (addFMODSource, [gameObjects, "fountain.png", "0879_on_Exh.ogg"])], 0xaaaaaa)
gameObjects.append(popUp)

#------------------MAIN LOOP-----------------------------
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

    #dumps data into the screen
    lastFrameTime = currentTime
    pygame.display.update()
    clock.tick(30)

#------------------------------------QUIT------------------------
pygame.display.quit()
pygame.quit()
FMOD.release()
sys.exit()
