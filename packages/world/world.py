from packages.area.area import Area
from packages.transition.transition import transition;
from packages.player.player import player;
from pygame import mixer
import time

import sys



class World:

    NORTH = 1
    SOUTH = 2
    EAST = 3
    WEST = 4
    UP = 5
    DOWN = 6
    NORTH_EAST = 7
    SOUTH_EAST = 8
    SOUTH_WEST = 9
    NORTH_WEST = 10


    #AUTHOR METHODS
    def __init__(self,name, description = "New World", player = player(),loadScript = ""):
        self.name = name
        self.description = description
        self.player = player
        self.areas = []
        self.loadScript = loadScript;
        if self.loadScript != "":
            self.loadScript()



    #Creates a new area unless one with the given name already exists
    #Returns the area object to the author.
    def newArea(self, name, description):
        if not self.areaExists(name):
            area = Area(name, description)
            self.areas.append(area)
            #if tisis the only area in the world then set the players area to it
            if len(self.areas)== 1:
                self.player.currentArea = self.areas[0]
        else:
            raise Exception("Duplicate area " + name + " cannot be created.")
        return area


    def newTransition(self, name, areaIn, destinationOut, isTwoWay, description = "It must lead somewhere"):

        areaFound = False
        destinationFound = False
        targetArea = None
        targetDestination = None

        #areaIn will be in the form ["quarry", "northeast"] meaning they want a new transition in the northeast of the quarry
        area = areaIn[0]
        areaDirection = areaIn[1]

        #destinationOut will be in the form ["river", "south"] meaning the transition will lead to the south of the quarry
        destination = destinationOut[0]
        destinationDirection = destinationOut[1]

        #ERROR CHECKING UP FRONT
        #checking for existence of target area
        areaFound = self.areaExists(area)
        if areaFound == False:
            raise Exception("Area " + area + " does not exist")

        if area == "wood":
            print "Why"
        targetArea = self.getArea(area)

        #checking for existence of target destination
        destinationFound = self.areaExists(destination)
        if destinationFound == False:
            raise Exception("Destination " + destination + " does not exist")
        targetDestination = self.getArea(destination)

        #checking if directions given are valid
        if not self.validDirection(areaDirection):
            raise Exception("Direction " + areaDirection + " does not exist")
        if not self.validDirection(destinationDirection):
            raise Exception("Direction " + destinationDirection + " does not exist")

        areaDirection = self.trimDirectionString(areaDirection);
        destinationDirection = self.trimDirectionString(destinationDirection);

        #make transition in targetArea
        targetAreaTransition = transition(name, targetArea, areaDirection, targetDestination, True, description)
        targetArea.newTransition(targetAreaTransition)

        if isTwoWay:
            #make transition in destination with ability to come back through
            destinationTransition = transition(name, targetDestination, destinationDirection, targetArea, True, description)
            targetDestination.newTransition(destinationTransition)
        else:
            #make transition in destination without ability to come back through
            destinationTransition = transition(name, targetDestination, destinationDirection, targetArea, False, description)
            targetDestination.newTransition(destinationTransition)

    def movePlayer(self,target):

            playerMoved = False
            destination = ""
            player = self.player
            if self.validDirection(target):
                target = self.trimDirectionString(target)
                for area in self.areas:
                    if player.currentArea.name == area.name and playerMoved == False:
                        if self.validRoute(area,target)[0]:
                            transition = self.validRoute(area,target)[1]
                            if transition.isPassable:
                                player.currentArea = transition.destination
                                playerMoved = True
                            else:
                                print "I cannot go through the " + transition.name
                        else:
                            print "There is no route that leads " + target
            elif self.validTransition(target,player.currentArea)[0]:
                            transition = self.validTransition(target,player.currentArea)[1]
                            if transition.isPassable:
                                player.currentArea = transition.destination
                                playerMoved = True
                            else:
                                print "I cannot go through the " + transition.name
            else:
                print target + " is not a place you can go"

        #    if playerMoved:
            #    print "Player is in " + player.currentArea.name


# HELPER METHODS

    #Searches the area for a transition that allows the user to go a specific direction.
    #returns True and transition object as a tuple if transitionis found that provides the route down that direction
    #EXAMPLE:
    #          Area:
    #               house
    #               house.transitions = [Door]
    #
    #     Transition: Door
    #               Door.direction = "northeast"
    #If the arguments to the function are house and northeast then it will return True since the door provides the route to the norheast

    def validRoute(self, area, targetDirection):
        for transition in area.transitions:
             if transition.direction == targetDirection:
                 return (True,transition)
        return False, None

    #Searches the given area for the given transition
    #Returns True if transition is found False otherwisee
    def validTransition(self, name, area):
        for transition in area.transitions:
             if name == transition.name:
                return True, transition
        return False, None;


    #Searches for the name of the area in the list of areas (self.areas) in the world.
    #Returns area object once found.
    def getArea(self,name):
        if self.areaExists(name):
            for area in self.areas:
                if name == area.name:
                    return area
        else:
            raise exception("Area " + name + "does not exist")


    #Searches for existence of an area with given name
    #Returns True if found, False otherwise
    def areaExists(self, name):
        for area in self.areas:
            if area.name == name:
                return True
        return False

    #checks to see if direction givenis a valid direction
    #returns True if valid False otherwise
    def validDirection(self, direction):
        validDirection = False;
        direction = self.trimDirectionString(direction.lower())

        if direction == "north":
            validDirection = True
        elif direction == "east":
            validDirection = True
        elif direction == "south":
            validDirection = True
        elif direction == "west":
            validDirection = True
        elif direction == "northeast":
            validDirection = True
        elif direction == "southeast":
            validDirection = True
        elif direction == "southwest":
            validDirection = True
        elif direction == "northwest":
            validDirection = True
        elif direction == "up":
            validDirection = True
        elif direction == "down":
            validDirection = True

        return validDirection;

    #trims all spaces from direction string and casts it to lower case
    #returns the result string
    def trimDirectionString(self, direction):
        direction = direction.lower()
        return "".join(direction.split())

    def printWorld(self):
        print(self.description)
        for x in range(len(self.description)):
            sys.stdout.write("-")
        print ""
        print("Areas: ")
        for area in self.areas:
            Area.printArea(area, area.name)
            if self.player.currentArea.name == area.name:
                self.player.printPlayer();

            print "\t------------------------------------------------------------------------"
