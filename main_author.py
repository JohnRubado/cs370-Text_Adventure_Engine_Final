from packages.world.world import *;
import os
import time as t

#LIBRARIES INCLUDED BY AUTHOR
from pygame import *
from PIL import Image

if os.path.dirname(__file__) != "":
    os.chdir(os.path.dirname(__file__))


mixer.init()


def waterfallScript():
    cave = mixer.Sound("./sounds/waterfall.wav")
    cave.play()


def pathScript():
    walking = mixer.Sound("./sounds/walking.wav")
    walking.play()

def swordScript():
    sword = mixer.Sound("./sounds/sword.wav")
    sword.play()

def fallPicture():
    image = Image.open("./pictures/fallPic.png")
    image.show()



#this script dynamically updates the players health.
def fallScript():
    fall = mixer.Sound("./sounds/manfall.wav")
    fall.play()
    player = myWorld.getPlayer()
    player.health = player.health - 50
    print "You lose 50 health."
    if player.health <= 0:
        print "You have died."
        t.sleep(3)
        myWorld.quitGame()

def wallcrackScript():
    collapse = mixer.Sound("./sounds/wallcrack.wav")
    collapse.play()
    print "THE CRACK OPENS AND THE CAVE BEGINS COLLAPSING. YOU NEARLY ESCAPE BY SLIDING THROUGH THE CRACK."
    myWorld.movePlayer("pedestal")
    outPedestal = myWorld.getTransition("pedestal", "Treasure Beach")
    outPedestal.name = "wall opening"
    outPedestal.description = "an opening in the wall that you slipped through."

#This script interacts with the user and asks them if theyd like to end the game.
def endGameScript():
    print "The necklace imbues you with the power to escape. Do you wish to escape this reality?"
    answer = raw_input()

    while answer.strip() != "yes" and answer.strip() != "no":
        print "yes or no. You're so close to freedom!"
        answer = raw_input()


    if answer.strip() == "yes":
        print "You disintegrate into the 1's and 0's from which you were born. Free at last!!"
        myWorld.quitGame()
    if answer.strip() == "no":
        print "Fair enough. Enjoy the rest of eternity on this beach."

#This is an example script that updates the world dynamically during play.
#This one specifically updates the waterfall that is inside the cave, so that when the user places a ladder
#on the quarry waterfall, the cave waterfall behaves differently.
def caveWaterfallScript():
    waterfall = myWorld.getTransition("waterfall","cave")
    waterfall.description = "The water is flowing very fast, you can barely reach the ladder."
    waterfall.onSuccessScripts = []
    waterfall.onSuccess = "You climb down the ladder and nearly slip."

#Here we are dynamically updating the players score when they succesfully use the ladder to get up
#the quarry side of the waterfall.
#Here we show that we can force certain functionalities within scripts. Normally using an item would leave it in your inventory,
#but here since its a ladder, we want it to be placed in the spot its needed, and then removed from the game.
def useLadderScript():
    player = myWorld.getPlayer()
    player.score = player.score + 10
    player.removeFromInventory("ladder")
    print "+10 score."


#CREATE THE WORLD AND THE PLAYER
thePlayer = player("Johnny", "A young man")
myWorld = World("The Narrows","An uncharted territory. Good Luck.",thePlayer);

#CREATE SOME AREAS
quarry = myWorld.newArea("quarry", "Placeholder description")
quarry.setDescription("There are many rocks around here")
woods = myWorld.newArea("woods", "Many trees surround the area, wild animals can be heard")
cave = myWorld.newArea("cave", "Its dark and wet")
treasureBeach = myWorld.newArea("Treasure Beach","There is a large beach with a wrecked ship and shiny golden treasure everywhere!")
#CREATE SOME TRANSITIONS

inPath, outPath = myWorld.newTransition("path",["quarry", "west"], ["woods", "north"], True, "Its covered with giant boulders. I can't get by.")
inCavern, outCavern = myWorld.newTransition("cavern",["woods", "east"], ["cave", "west"], False, "Its narrow and dark inside and a rock is blocking my way, I wonder where it leads?")
inWaterfall, outWaterfall = myWorld.newTransition("waterfall",["cave", "north"], ["quarry", "south"], True, "Its flowing very fast.")
inPedestal, outPedestal = myWorld.newTransition("pedestal", ["cave","south"],["Treasure Beach","north"] ,False, "Its an ancient pedestal, it sits in front of a large crack in the wall.")

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
inPedestal.requirements.append("pie")



#SET MESSAGES TO BE DISPLAYED ON SUCCESS OR FAILURE
inCavern.onSuccess = "You slide down the narrow cavern. You definitely can't get back out"
inCavern.detailedDescription = "You see a lot of rat poop."
outCavern.onFailure = "You try, but its too steep"
outCavern.description = "The light is beaming in from above, there must be another way out."


inWaterfall.onSuccess = "You wake up gasping for air. You must have fallen out of the waterfall and hit your head."
outWaterfall.onFailure= "The rocks are too slippery to go up."
outWaterfall.requirements.append("ladder")
outPedestal.onFailure = "You try, but its too steep to go back up."

rock = myWorld.newItem("rock", "it's an ugly small rock", "quarry", False)
rock.onFailure = "Its a pretty lame rock, you decide not to carry such dead weight."

sword = myWorld.newItem("sword", "A dull longsword", "quarry")
sword.onSuccess = "You take the sword, its a bit dull but it should do the job."
sword.detailedDescription = "As you look closely, you see old dried blood along the edge."
sword.onSuccessScripts.append(swordScript)

pickaxe = myWorld.newItem("pickaxe", "A hefty pickaxe.", "quarry")
pickaxe.onUse = "You swing the pickaxe with all your might. The way is cleared."

ladder = myWorld.newItem("ladder", "A sturdy ladder.", "woods")
ladder.onUse = "You lean the ladder against the rocks."
ladder.onUseScripts.append(useLadderScript)
ladder.onUseScripts.append(caveWaterfallScript)

pie = myWorld.newItem("pie", "A warm pie, I wonder who made it?", "woods")
pie.detailedDescription = "A closer look reveals that the ants must have found it first.."
pie.onUseScripts.append(wallcrackScript)

necklace = myWorld.newItem("necklace", "A beautiful golden necklace with thousands of markings.","Treasure Beach")
necklace.onSuccessScripts.append(endGameScript)

myWorld.startGame()
