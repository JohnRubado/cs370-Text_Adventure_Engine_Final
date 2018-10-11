from packages.world.world import *;
from packages.parser.parser import parser
from pygame import mixer

mixer.init()

def onLoadScript():
    birds = mixer.Sound("birds.wav")
    birds.play()

script = onLoadScript

#CREATE THE WORLD AND THE PLAYER
player = player("Johnny", "A young man")
myWorld = World("The Narrows","An uncharted territory. Good Luck.",player, script);

#CREATE SOME AREAS
quarry = myWorld.newArea("quarry", "Placeholder description")
quarry.setDescription("There are many rocks around here")
woods = myWorld.newArea("woods", "Many trees surround the area, wild animals can be heard")
cavern = myWorld.newArea("cave", "Its dark and wet")

#CREATE SOME TRANSITIONS
myWorld.newTransition("path",["quarry", "west"], ["woods", "north"], True, "Its covered with giant boulders.")
inCavern, outCavern = myWorld.newTransition("cavern",["woods", "east"], ["cave", "west"], False, "Its narrow and dark inside, I wonder where it leads?")
inWaterfall, outWaterfall = myWorld.newTransition("waterfall",["cave", "north"], ["quarry", "south"], False, "Its flowing very fast.")


#SET MESSAGES TO BE DISPLAYED ON SUCCESS OR FAILURE
inCavern.onSuccess = "You slide down the narrow cavern. You definitely can't get back out"
outCavern.onFailure = "Too steep"
outCavern.description = "The light is beaming in from above, there must be another way out."

inWaterfall.onSuccess = "You wake up gasping for air. You must have fallen out of the waterfall and hit your head."
outWaterfall.onFailure= "The rocks are too slippery to go up."

parser = parser(myWorld)
parser.start()
