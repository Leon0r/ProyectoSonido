import sys
import pygame
from GameObjects.PopUpMenu import PopUpMenu
from GameObjects.FMODSource import FMODSource
from GameObjects.FMODListener import FMODListener
from GameObjects.FMODReverb import FMODReverb
from GameObjects.FMODGeometry import FMODGeometry
from Utils.ResourcesManager import ResourcesManager
from Utils.Utils import getStringCurrentWorkingDirectory
from FMODManagement.FMOD import FMOD
from pyfmodex.flags import MODE

# --------------------------CALLBACKS------------


def callBackTest(f, a, _object):
    print(str(_object.getX()) + f + str(a))  # example of getting variable
    # parameters of an object


def removeLastElementInserted(gameObjects, _object):
    if len(gameObjects) < 2:  # cant remove the pop up menu
        print("Can't remove element from empyt list")
        return

    gameObjects[0].release()
    gameObjects.remove(gameObjects[0])


def addFMODSource(gameObjects, imageName, soundName, _object):
    fmodSource = FMODSource(resourcesManager.getSound(
        soundName), MODE.LOOP_NORMAL | MODE.THREED)
    fmodSource.setSpriteFromImage(resourcesManager.getImage(imageName))
    fmodSource.setPosition((_object.getX(), _object.getY()))
    # inserts the element at tht beggining of the list
    gameObjects.insert(0, fmodSource)


def addFMODListener(gameObjects, imageName, _object):
    fmodListener = FMODListener()
    fmodListener.setSpriteFromImage(resourcesManager.getImage(imageName))
    fmodListener.setPosition((_object.getX(), _object.getY()))
    # inserts the element at tht beggining of the list
    gameObjects.insert(0, fmodListener)


def addFMODReverb(gameObjects, imageName, _object):
    fmodReverb = FMODReverb()
    fmodReverb.setSpriteFromImage(resourcesManager.getImage(imageName))
    fmodReverb.setPosition((_object.getX(), _object.getY()))
    # inserts the element at tht beggining of the list
    gameObjects.insert(0, fmodReverb)


def addFMODGeometry(gameObjects, imageName, _object):
    fmodGeometry = FMODGeometry()
    fmodGeometry.setSpriteFromImage(resourcesManager.getImage(imageName))
    fmodGeometry.setPosition((_object.getX(), _object.getY()))
    # inserts the element at tht beggining of the list
    gameObjects.insert(0, fmodGeometry)


# -------------------PYGAME-------------------------
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
pygame.display.set_caption("Proyecto Sonido")
pygame.font.init()
x = 0

# -------------------FMOD--------------------------
FMOD.init()
FMOD.setRollOffScale(0.1)

# -------------------RESOURCES----------------------
resourcesManager = ResourcesManager.getInstance()
resourcesManager.loadImagesFromDirectory(
    getStringCurrentWorkingDirectory() + "\\resources\\sprites")
resourcesManager.loadSoundsFromDirectory(
    getStringCurrentWorkingDirectory() + "\\resources\\sounds")

# -------------------GAME OBJECTS-------------------------
gameObjects = []
popUp = PopUpMenu(["Add Listener", "Add Source", "Add Reverb", "Remove last element"],
                  [(addFMODListener, [gameObjects, "Listener.png"]),
                   (addFMODSource, [gameObjects, "Source.png", "steps0.wav"]),
                   (addFMODReverb, [gameObjects, "Reverb.png"]),
                   (removeLastElementInserted, [gameObjects])], 0xccedf3)

gameObjects.append(popUp)

# ------------------MAIN LOOP-----------------------------
running = True
handled = False
lastFrameTime = pygame.time.get_ticks()
while running:
    # clear
    screen.fill(0x889ea2)
    # get events
    for e in pygame.event.get():
        handled = False
        if e.type == pygame.QUIT:
            running = False
            handled = True
            break

        for gameObject in gameObjects:
            handled = gameObject.handleInput(e)
            if handled:
                break

    currentTime = pygame.time.get_ticks()
    # deltaTime in seconds.
    deltaTime = (currentTime - lastFrameTime) / 1000.0
    # update
    for gameObject in gameObjects:
        gameObject.update(deltaTime)

    # render
    for gameObject in gameObjects:
        gameObject.render(screen)

    # dumps data into the screen
    lastFrameTime = currentTime
    pygame.display.update()
    FMOD.update()
    clock.tick(30)

# ------------------------------------QUIT------------------------
for gameObject in gameObjects:
    gameObject.release()
resourcesManager.release()
FMOD.release()
pygame.display.quit()
pygame.quit()
sys.exit()
