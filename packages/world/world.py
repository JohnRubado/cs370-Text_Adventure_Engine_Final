from packages.area.area import Area
from packages.transition.transition import transition;
from packages.player.player import player;


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
    def __init__(self, description = "New World", player = player()):
        self.description = description
        self.player = player
        self.areas = []

    #Creates a new area unless one with the given name already exists
    #Returns the area object to the author.
    def newArea(self, name, description):
        if not self.areaExists(name):
            area = Area.newArea(self, name, description)
            self.areas.append(area)

        return self.getArea(name)


    def newTransition(self, name, area, direction, destination, isTwoWay, description = "It must lead somewhere"):

        areaFound = False
        destinationFound = False
        targetArea = None
        targetDestination = None

        #ERROR CHECKING UP FRONT
        #checking for existence of target area
        areaFound = self.areaExists(area)
        if areaFound == False:
            raise Exception("Area " + area + " does not exist")
        targetArea = self.getArea(area)

        #checking for existence of target destination
        destination = self.areaExists(destination)
        if destinationFound == False:
            raise Exception("Destination " + destination + " does not exist")
        targetDestination = self.getArea(destination)

        if isTwoWay == False:
            newTransition = transition(name, targetArea, direction, targetDestination, description)
            targetArea.newTransition(newTransition)
        if isTwoWay == True:
            newTransition = transition(name, targetArea, direction, targetDestination, description)
            targetArea.newTransition(newTransition)

            if cardinalPosition == "east":
                self.newTransition(name, area, "west", destination, False, description)
            elif cardinalPosition == "west":
                self.newTransition(name, area, "east", destination, False, description)
            elif cardinalPosition == "north":
                self.newTransition(name, area, "south", destination, False, description)
            elif cardinalPosition == "south":
                self.newTransition(name, area, "north", destination, False, description)
            elif cardinalPosition == "northeast":
                self.newTransition(name, area, "southwest", destination, False, description)
            elif cardinalPosition == "southeast":
                self.newTransition(name, area, "northwest", destination, False, description)
            elif cardinalPosition == "southwest":
                self.newTransition(name, area, "northeast", destination, False, description)
            elif cardinalPosition == "northwest":
                self.newTransition(name, area, "southeast", destination, False, description)

    def movePlayer(self,target):

            playerMoved = False;
            destination = "";
            player = self.player;
            if self.validCardinalDirection(cardinalDirection):
                for area in self.areas:
                    if player.currentArea == area.name and playerMoved == False:
                        if cardinalDirection == "north":
                            if area.directions[self.NORTH].transition != None:
                                destination = area.directions[self.NORTH].transition.destination;
                                player.currentArea = destination;
                                print "You have taken the " + area.directions[self.NORTH].transition.name + " in the " + cardinalDirection;
                                playerMoved = True;
                            else:
                                print "There is no route that leads " + cardinalDirection;
                        elif cardinalDirection == "east":
                            if area.directions[self.EAST].transition != None:
                                destination = area.directions[self.EAST].transition.destination;
                                player.currentArea = destination;
                                print "You have taken the " + area.directions[self.EAST].transition.name + " in the " + cardinalDirection;
                                playerMoved = True;
                            else:
                                print "There is no route that leads " + cardinalDirection;
                        elif cardinalDirection == "south":
                            if area.directions[self.SOUTH].transition != None:
                                destination = area.directions[self.SOUTH].transition.destination;
                                player.currentArea = destination;
                                print "You have taken the " + area.directions[self.SOUTH].transition.name + " in the " + cardinalDirection;
                                playerMoved = True;
                            else:
                                print "There is no route that leads " + cardinalDirection;
                        else:
                            if area.directions[self.WEST].transition != None:
                                destination = area.directions[self.WEST].transition.destination;
                                player.currentArea = destination;
                                print"You have taken the " + area.directions[self.WEST].transition.name + " in the " + cardinalDirection;
                                playerMoved = True;
                            else:
                                print "There is no route that leads " + cardinalDirection;

            else:
                print "What is " +cardinalDirection + "? there is no " + cardinalDirection;

            if playerMoved == True:
                self.look();
# HELPER METHODS
    #Searches for the name of the area in the list of areas (self.areas) in the world.
    #Returns area object once found.
    def getArea(self,name):
        if self.areaExists(name):
            for area in self.areas:
                if name is area.name:
                    return area
        else:
            raise exception("Area " + name + "does not exist")


    #Searches for existence of an area with given name
    #Returns true if found, false otherwise
    def areaExists(self, name):
        for area in self.areas:
            if area.name == name:
                return True
        return False

    def validDirection(self, direction):
        validDirection = False;
        direction =direction.lower();
        if direction is "north":
            validDirection = True
        elif direction is "east":
            validDirection = True
        elif direction is "south":
            validDirection = True
        elif direction is "west":
            validDirection = True
        elif direction is "northeast":
            validDirection = True
        elif direction is "southeast":
            validDirection = True
        elif direction is "southwest":
            validDirection = True
        elif direction is "northwest":
            validDirection = True
        elif direction is "up":
            validDirection = True
        elif direction is "down":
            validDirection = True
        return validCardinalDir;

    #trims all spaces from direction string and casts it to lower case
    #returns the result string
    def trimDirectionString(self, direction):
        return "".join(direction.split())
