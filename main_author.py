from packages.world.world import *;


#LIBRARIES INCLUDED BY AUTHOR
from pygame import *
from PIL import Image

mixer.init()

def onLoadScript():
     birds = mixer.Sound("./sounds/birds.wav")
     birds.play()

def waterfallScript():
    cave = mixer.Sound("./sounds/waterfall.wav")
    cave.play()

def fallScript():
    fall = mixer.Sound("./sounds/manfall.wav")
    fall.play()

def pathScript():
    walking = mixer.Sound("./sounds/walking.wav")
    walking.play()

def swordScript():
    sword = mixer.Sound("./sounds/sword.wav")
    sword.play()

def fallPicture():
    image = Image.open("./pictures/fallPic.png")
    image.show()


# TODO:
# Add tests for inventory functionality.
# Complete design doc with ability to map tests to it.




#
# thePlayer = player("NOOB", "THE NOOBEST")
# myWorld = World("BLANK WORLD", "BLANKEST OF WORLDS",thePlayer)

#CREATE THE WORLD AND THE PLAYER
thePlayer = player("Johnny", "A young man")
myWorld = World("The Narrows","An uncharted territory. Good Luck.",thePlayer,onLoadScript);

#CREATE SOME AREAS
quarry = myWorld.newArea("quarry", "Placeholder description")
quarry.setDescription("There are many rocks around here")
woods = myWorld.newArea("woods", "Many trees surround the area, wild animals can be heard")
cave = myWorld.newArea("cave", "Its dark and wet")

#CREATE SOME TRANSITIONS

inPath, outPath = myWorld.newTransition("path",["quarry", "west"], ["woods", "north"], True, "Its covered with giant boulders. I can't get by.")
inCavern, outCavern = myWorld.newTransition("cavern",["woods", "east"], ["cave", "west"], False, "Its narrow and dark inside and a rock is blocking my way, I wonder where it leads?")
inWaterfall, outWaterfall = myWorld.newTransition("waterfall",["cave", "north"], ["quarry", "south"], False, "Its flowing very fast.")

#SETTING SOME SCRIPTS TO BE EXECUTED
inWaterfall.onSuccessScripts.append(fallScript)
inWaterfall.onSuccessScripts.append(fallPicture)
inPath.onSuccessScripts.append(pathScript)
inPath.onFailure = "You can't use the path, it is blocked by large boulders."
inPath.openedDescription = "It is covered with many small rocks."
outPath.onSuccessScripts.append(pathScript)
outPath.description = "It is covered with many small rocks."
inCavern.openedDescription = "Its narrow and dark inside and I can barely fit through. I wonder where it leads."

#SETTING SOME TRANSITION requirements
inPath.requirements.append("pickaxe")
inCavern.requirements.append("pickaxe")



#SET MESSAGES TO BE DISPLAYED ON SUCCESS OR FAILURE
inCavern.onSuccess = "You slide down the narrow cavern. You definitely can't get back out"
inCavern.detailedDescription = "You see a lot of rat poop."
outCavern.onFailure = "You try, but its too steep"
outCavern.description = "The light is beaming in from above, there must be another way out."


inWaterfall.onSuccess = "You wake up gasping for air. You must have fallen out of the waterfall and hit your head."
outWaterfall.onFailure= "The rocks are too slippery to go up."


rock = myWorld.newItem("rock", "it's an ugly small rock", "quarry", False)
rock.onFailure = "Its a pretty lame rock, you decide not to carry such dead weight."

sword = myWorld.newItem("sword", "A dull longsword", "quarry")
sword.onSuccess = "You take the sword, its a bit dull but it should do the job."
sword.detailedDescription = "As you look closely, you see old dried blood along the edge."
sword.onSuccessScripts.append(swordScript)

pickaxe = myWorld.newItem("pickaxe", "A hefty pickaxe.", "quarry")
pickaxe.onUse = "You swing the pickaxe with all your might. The way is cleared."



pie = myWorld.newItem("pie", "A warm pie, I wonder who made it?", "woods")
pie.detailedDescription = "A closer look reveals that the ants must have found it first.."

myWorld.startGame()
