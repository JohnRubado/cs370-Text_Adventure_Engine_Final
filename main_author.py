from packages.world.world import *;

from pygame import *
from PIL import Image

mixer.init()

def onLoadScript():
     birds = mixer.Sound("sounds/birds.wav")
     birds.play()

def waterfallScript():
    cave = mixer.Sound("sounds/waterfall.wav")
    cave.play()
def fallScript():
    fall = mixer.Sound("sounds/manfall.wav")
    fall.play()

def pathScript():
    walking = mixer.Sound("sounds/walking.wav")
    walking.play()

def fallPicture():
    image = Image.open("pictures/fallPic.png")
    image.show()






#
# player = player("NOOB", "THE NOOBEST")
# myWorld = World("BLANK WORLD", "BLANKEST OF WORLDS")

#CREATE THE WORLD AND THE PLAYER
player = player("Johnny", "A young man")
myWorld = World("The Narrows","An uncharted territory. Good Luck.",player,onLoadScript);

#CREATE SOME AREAS
quarry = myWorld.newArea("quarry", "Placeholder description")
quarry.setDescription("There are many rocks around here")
woods = myWorld.newArea("woods", "Many trees surround the area, wild animals can be heard")
cave = myWorld.newArea("cave", "Its dark and wet")

#CREATE SOME TRANSITIONS

inPath, outPath = myWorld.newTransition("path",["quarry", "west"], ["woods", "north"], True, "Its covered with giant boulders.")
inCavern, outCavern = myWorld.newTransition("cavern",["woods", "east"], ["cave", "west"], False, "Its narrow and dark inside, I wonder where it leads?")
inWaterfall, outWaterfall = myWorld.newTransition("waterfall",["cave", "north"], ["quarry", "south"], False, "Its flowing very fast.")

#SETTING SOME SCRIPTS TO BE EXECUTED
inWaterfall.onSuccessScripts.append(fallScript)
inWaterfall.onSuccessScripts.append(fallPicture)
inPath.onSuccessScripts.append(pathScript)
outPath.onSuccessScripts.append(pathScript)
#SET MESSAGES TO BE DISPLAYED ON SUCCESS OR FAILURE
inCavern.onSuccess = "You slide down the narrow cavern. You definitely can't get back out"
outCavern.onFailure = "You try, but its too steep"
outCavern.description = "The light is beaming in from above, there must be another way out."


inWaterfall.onSuccess = "You wake up gasping for air. You must have fallen out of the waterfall and hit your head."
outWaterfall.onFailure= "The rocks are too slippery to go up."


myWorld.newItem("rock", "it's a small rock", "quarry", False)
myWorld.newItem("sword", "Yeah, that's a sword", "quarry", True)
myWorld.newItem("pie", "Yum, yum, yum, a pie", "woods", True)

myWorld.startGame()
