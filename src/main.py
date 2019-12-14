import sys
import pygame
from GameObjects.PopUpMenu import PopUpMenu
from GameObjects.FMODSource import FMODSource
from GameObjects.FMODListener import FMODListener
from GameObjects.FMODReverb import FMODReverb
from Utils.ResourcesManager import ResourcesManager
from Utils.Utils import getStringCurrentWorkingDirectory
from FMODManagement.FMOD import FMOD
from pyfmodex.flags import MODE

#--------------------------CALLBACKS------------
def callBackTest(f, a, _object):
    print(str(_object.getX()) + f + str(a)) #example of getting variable
    #parameters of an object

def addFMODSource(gameObjects, imageName, soundName, _object):
    fmodSource= FMODSource(resourcesManager.getSound(soundName), MODE.LOOP_NORMAL | MODE.THREED)
    fmodSource.setSpriteFromImage(resourcesManager.getImage(imageName))
    fmodSource.setPosition((_object.getX(), _object.getY()))
    gameObjects.insert(0, fmodSource) #inserts the element at tht beggining of the list

def addFMODListener(gameObjects, imageName, _object):
    fmodListener = FMODListener()
    fmodListener.setSpriteFromImage(resourcesManager.getImage(imageName))
    fmodListener.setPosition((_object.getX(), _object.getY()))
    gameObjects.insert(0, fmodListener) #inserts the element at tht beggining of the list

def addFMODReverb(gameObjects, imageName, _object):
    fmodReverb = FMODReverb()
    fmodReverb.setSpriteFromImage(resourcesManager.getImage(imageName))
    #fmodReverb.setPosition((_object.getX(), _object.getY()))
    gameObjects.insert(0, fmodReverb) #inserts the element at tht beggining of the list

#-------------------PYGAME-------------------------
screen = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()
pygame.display.set_caption("Hello World")
pygame.font.init()
x = 0

#-------------------FMOD--------------------------
FMOD.init()
FMOD.setRollOffScale(0.1)
#-------------------RESOURCES----------------------
resourcesManager = ResourcesManager()
resourcesManager.loadImagesFromDirectory(getStringCurrentWorkingDirectory() + "\\resources\\sprites")
resourcesManager.loadSoundsFromDirectory(getStringCurrentWorkingDirectory() + "\\resources\\sounds")

#-------------------GAME OBJECTS-------------------------
gameObjects = []
popUp = PopUpMenu(["Add Listener", "Add Source", "Add Reverb"], 
        [(addFMODListener, [gameObjects, "Listener.png"]), 
        (addFMODSource, [gameObjects, "Source.png", "0879_on_Exh.ogg"]),
        (addFMODReverb, [gameObjects, "Source.png"])], 0xaaaaaa)

gameObjects.append(popUp)

#------------------MAIN LOOP-----------------------------
running = True
lastFrameTime = pygame.time.get_ticks()
while running:
    #clear
    screen.fill(0x889ea2)
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
    FMOD.update()
    clock.tick(30)

#------------------------------------QUIT------------------------
pygame.display.quit()
pygame.quit()
FMOD.release()
sys.exit()
