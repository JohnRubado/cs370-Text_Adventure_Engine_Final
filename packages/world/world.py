from packages.area.area import Area
from packages.transition.transition import transition
from packages.player.player import player
from packages.parser.parser import parser
from packages.item.item import item
import json
import time
import sys
import dill as pickle



class World:


    #AUTHOR METHODS
    def __init__(self,name, description = "New World", player = player(),loadScript = ""):
        self.name = name
        self.description = description
        self.player = player
        self.areas = []
        self.loadScript = loadScript;


    #Serializes all of the world into JSON format for later loading
    def saveProgress(self):
        saveFile = open("./"+ self.player.name + ".txt", 'wb')
        print "Saving . . . "
        world = {"name": self.name,
        "description":self.description,
        "areas": [],
        "player": {"name": self.player.name,
        "description":self.player.description,
        "currentArea":self.player.currentArea.name,
        "inventory":[]}}

        #save items in players inventory
        for item in self.player.inventory:
            currItem = {"name":item.name,
                        "description":item.description,
                        "area":None,
                        "moveable": item.moveable,
                        "onSuccess": item.onSuccess,
                        "onFailure": item.onFailure,
                        "detailedDescription": item.detailedDescription,
                        "onSuccessScripts": [],
                        "onFailureScripts": [],
                        "onUse": item.onUse,
                        "onUseScripts": []
                        }
            #saving item scripts for items in players inventory
            for script in item.onSuccessScripts:
                serScript = pickle.dumps(script)
                currScript = {"script": serScript}
                currItem["onSuccessScripts"].append(currScript)
            for script in item.onFailureScripts:
                serScript = pickle.dumps(script)
                currScript = {"script": serScript}
                currItem["onFailureScripts"].append(currScript)
            for script in item.onUseScripts:
                serScript = pickle.dumps(script)
                currScript = {"script": serScript}
                currItem["onUseScripts"].append(currScript)

            world["player"]["inventory"].append(currItem)

        #save all the areas their transitions, and their items.
        for area in self.areas:
            currArea = {"name" : area.name,
            "description": area.description,
            "transitions": [],
            "items": []}
            for transition in area.transitions:
                currTransition = {"name": transition.name,
                "direction": transition.direction,
                "isPassable": transition.isPassable,
                "onSuccess": transition.onSuccess,
                "onFailure": transition.onFailure,
                "destination": transition.destination.name,
                "area": transition.area.name,
                "description":transition.description,
                "detailedDescription":transition.detailedDescription,
                "openedDescription": transition.openedDescription,
                "onSuccessScripts": [],
                "onFailureScripts": [],
                "onOpenScripts": [],
                "requirements": []}

                #serializing scripts with pickle.
                for script in transition.onSuccessScripts:
                    serScript = pickle.dumps(script)
                    currScript = {"script": serScript}
                    currTransition["onSuccessScripts"].append(currScript)
                for script in transition.onFailureScripts:
                    serScript = pickle.dumps(script)
                    currScript = {"script": serScript}
                    currTransition["onFailureScripts"].append(currScript)
                for script in transition.onOpenScripts:
                    serScript = pickle.dumps(script)
                    currScript = {"script": serScript}
                    currTransition["onOpenScripts"].append(currScript)

                #saving transition requirements
                for requirement in transition.requirements:
                    currRequirement = {"requirement": requirement}
                    currTransition["requirements"].append(currRequirement)


                currArea["transitions"].append(currTransition)
            for item in area.items:
                currItem = {"name":item.name,
                            "description":item.description,
                            "detailedDescription":item.detailedDescription,
                            "area":area.name,
                            "moveable": item.moveable,
                            "onSuccess": item.onSuccess,
                            "onFailure": item.onFailure,
                            "onSuccessScripts": [],
                            "onFailureScripts": [],
                            "onUse": item.onUse,
                            "onUseScripts": []}
                for script in item.onSuccessScripts:
                    serScript = pickle.dumps(script)
                    currScript = {"script": serScript}
                    currItem["onSuccessScripts"].append(currScript)
                for script in item.onFailureScripts:
                    serScript = pickle.dumps(script)
                    currScript = {"script": serScript}
                    currItem["onFailureScripts"].append(currScript)
                for script in item.onUseScripts:
                    serScript = pickle.dumps(script)
                    currScript = {"script": serScript}
                    currItem["onUseScripts"].append(currScript)

                currArea["items"].append(currItem)
            world["areas"].append(currArea)



        world = pickle.dump(world,saveFile)
        #world = json.dumps(world,indent=4, separators=(',', ': '))
        saveFile.close()
        print "Progress saved in " + self.player.name + ".txt"

        # for area in json.loads(world)["areas"]:
        #     for transition in area["transitions"]:
        #         print transition["name"] + " in " + transition["area"]
        #print world

    #Creates a new area unless one with the given name already exists
    #Returns the area object to the author.
    def newArea(self, name, description):
        if not self.areaExists(name):
            area = Area(name, description)
            self.areas.append(area)
            #if this is the only area in the world then set the players area to it
            if len(self.areas) == 1:
                self.player.currentArea = self.areas[0]
        else:
            raise Exception("Duplicate area " + name + " cannot be created.")
        return area

    def newItem(self, name, description, area, isMoveable = True):

        areaFound = self.areaExists(area)
        if areaFound == False:
            raise Exception("Area " + area + " does not exist")

        areaItem = self.getArea(area)

        item1 = item(name, description, area, isMoveable)
        areaItem.newItem(item1)

        return item1

    def pickUpItem(self, item):
        area = self.player.currentArea
        self.player.addToInventory(item)

    def useItem(self, itemName, transitionName):
        #check to see if transition exists.
        transExists,transition = self.validTransition(transitionName,self.player.currentArea)
        itemUsed = False
        hasItem = False
        if transExists:


            #check to see if player has item
            for item in self.player.inventory:
                if itemName == item.name:
                    hasItem = True
                    #check to see if item is a requirement
                    for requirement in transition.requirements:
                        if requirement == item.name:
                            itemUsed = True
                            transition.requirements.remove(requirement)
                            print item.onUse

                            for script in item.onUseScripts:
                                script()
                            for script in transition.onOpenScripts:
                                script()

            if hasItem == False:
                print "You do not have a " + itemName
            else:
                if itemUsed == False:
                    print transitionName + " does not require a " + itemName




        else:
            print "There is no " + transitionName


    def checkInventory(self):
        self.player.printInventory()

    def dropItem(self, targetItem):
        area = self.player.currentArea

        for item in self.player.inventory:
            if targetItem == item.name:
                self.player.dropFromInventory(item)
                self.player.currentArea.items.append(item)
                print("You drop the " + item.name)
                return

        print("You do not have a " + targetItem)


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

        return targetAreaTransition, destinationTransition

    def movePlayer(self,target):

            playerMoved = False
            destination = ""
            player = self.player
            transition = None
            if self.validDirection(target):
                target = self.trimDirectionString(target)
                for area in self.areas:
                    if player.currentArea.name == area.name and playerMoved == False:
                        if self.validRoute(area,target)[0]:
                            transition = self.validRoute(area,target)[1]
                            if transition.isPassable and transition.requirements == []:
                                player.currentArea = transition.destination
                                playerMoved = True
                        else:
                            print "There is no route that leads " + target
            elif self.validTransition(target,player.currentArea)[0]:
                            transition = self.validTransition(target,player.currentArea)[1]
                            if transition.isPassable and transition.requirements == []:

                                player.currentArea = transition.destination
                                playerMoved = True
            else:
                print target + " is not a place you can go"

            if playerMoved:
                if transition.onSuccess == None:
                    print "You use the " + transition.name + " that leads " + transition.direction.lower()
                else:
                    print transition.onSuccess

                #if there is a script to be executed


                if transition.onSuccessScripts != []:
                    for script in transition.onSuccessScripts:
                        script()
                if player.currentArea.inAreaScripts != []:
                    for script in player.currentArea.inAreaScripts:
                        script()

                self.displayAreaDescription()
            elif transition != None:
                if transition.onFailure == None:
                    print "You cannot traverse the " + transition.name
                else:
                    print transition.onFailure
                if transition.onFailureScripts != []:
                    for script in transition.onFailureScripts:
                        script()

    #Method will be called when player types look
    #Displays everything in the room
    def look(self, target = ""):
        isItem = False
        isTransition = False

        if len(self.areas) != 0:

            #Check if the target is an existing item near the player or in their inventory.
            #Or if the target is an existing transition
            for item in self.player.currentArea.items:
                if self.trimDirectionString(target) == item.name:
                    isItem = True
                    theItem = item
            #checking inventory of player
            for item in self.player.inventory:
                if self.trimDirectionString(target) == item.name:
                    isItem = True
                    theItem = item

            #checking transitions in area
            for transition in self.player.currentArea.transitions:
                if self.trimDirectionString(target) == transition.name:
                    isTransition = True
                    theTransition = transition

            if target == "":
                self.player.currentArea.printArea()
            elif target == "me":
                self.player.printPlayer()
            elif isItem:
                if theItem.detailedDescription == None:
                    theItem.printDescription()
                else:
                    print theItem.detailedDescription
            elif isTransition:
                if theTransition.detailedDescription == None:
                    theTransition.printDescription()
                else:
                    print theTransition.detailedDescription
            else:
                print "You dont see a " + target
        else:
            print "You are everywhere and nowhere all at once. BUT HOW???"

    #A method that allows for the player to quit the game when they want
    def quitGame(self):
        sys.exit(0)


    #A method that gives user a help menu when they type out "help"
    def helpUser(self):
        print "To quit the game, simply type 'quit'"
        print "To save or load type, 'save' or 'load [filename]'"
    #method will be called when a player enters an area
    #it just displays the area they are in and the description of the area.
    def displayAreaDescription(self):
        print "You find yourself in the " + self.player.currentArea.name;
        print  self.player.currentArea.description

    #calling this method starts a new game.
    def startGame(self, isNew = True):
        play = parser(self)
        play.start(isNew)

    #calling this method loads a previous game from the save file given. Save file
    #should have been constructed with pickle.
    def loadGame(self, fileName, testing = False):

        #read world data from file
        try:
            with open(fileName, "rb") as f:
                data = pickle.load(f)
        except:
            print "Invalid file given. File should be created from typing save in game"
            return

        print "Loading . . ."

        #redefining world properties
        self.areas = []
        self.player = player(data["player"]["name"],data["player"]["description"], [])

        #set world properties
        self.name = data["name"]
        self.description = data["description"]

        #make all areas
        for area in data["areas"]:
            self.newArea(area["name"],area["description"])


        #set the players properties.
        self.player.name = data["player"]["name"]
        self.player.description = data["player"]["description"]
        self.player.currentArea = self.getArea(data["player"]["currentArea"])

        #with the area objects we can now make the desired transitions, and items
        for area in data["areas"]:
            for transitionMap in area["transitions"]:
                newTrans = transition(transitionMap["name"],self.getArea(transitionMap["area"]),transitionMap["direction"],self.getArea(transitionMap["destination"]), transitionMap["isPassable"],transitionMap["description"])
                newTrans.onSuccesScripts = []
                newTrans.onFailureScripts = []
                newTrans.requirements = []
                newTrans.onSuccess = transitionMap["onSuccess"]
                newTrans.onFailure = transitionMap["onFailure"]
                newTrans.openedDescription = transitionMap["openedDescription"]
                newTrans.detailedDescription = transitionMap["detailedDescription"]

                for script in transitionMap["onSuccessScripts"]:
                    currScript = pickle.loads(script["script"])
                    newTrans.onSuccessScripts.append(currScript)
                for script in transitionMap["onFailureScripts"]:
                    currScript = pickle.loads(script["script"])
                    newTrans.onSuccessScripts.append(currScript)
                for script in transitionMap["onOpenScripts"]:
                    currScript = pickle.loads(script["script"])
                    newTrans.onOpenScripts.append(currScript)


                for requirement in transitionMap["requirements"]:
                    newTrans.requirements.append(requirement["requirement"])

                newTrans.area.transitions.append(newTrans)

            #Loading items from save file
            for itemMap in area["items"]:
                newItem = self.newItem(itemMap["name"], itemMap["description"], area["name"], itemMap["moveable"])
                newItem.onSuccess = itemMap["onSuccess"]
                newItem.onFailure = itemMap["onFailure"]
                newItem.onUse = itemMap["onUse"]
                newItem.detailedDescription = itemMap["detailedDescription"]

                #loading scripts for area items
                for script in itemMap["onSuccessScripts"]:
                    currScript = pickle.loads(script["script"])
                    newItem.onSuccessScripts.append(currScript)
                for script in itemMap["onFailureScripts"]:
                    currScript = pickle.loads(script["script"])
                    newItem.onFailureScripts.append(currScript)
                for script in itemMap["onUseScripts"]:
                    currScript = pickle.loads(script["script"])
                    newItem.onUseScripts.append(currScript)

        #Loading the inventory
        for itemMap in data["player"]["inventory"]:
            newItem = item(itemMap["name"], itemMap["description"], None, itemMap["moveable"])
            newItem.onSuccess = itemMap["onSuccess"]
            newItem.onFailure = itemMap["onFailure"]
            newItem.onUse = itemMap["onUse"]
            for script in itemMap["onSuccessScripts"]:
                currScript = pickle.loads(script["script"])
                newItem.onSuccessScripts.append(currScript)
            for script in itemMap["onFailureScripts"]:
                currScript = pickle.loads(script["script"])
                newItem.onFailureScripts.append(currScript)
            for script in itemMap["onUseScripts"]:
                currScript = pickle.loads(script["script"])
                newItem.onUseScripts.append(currScript)
            self.player.inventory.append(newItem)





        if not testing:
            self.startGame(False)



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
    #Returns True and object if transition is found False otherwisee
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
        return "".join(direction.split())

    def printWorld(self):
        print(self.description)
        for x in range(len(self.description)):
            sys.stdout.write("-")
        print ""
        print("Areas: ")
        for area in self.areas:
            area.printArea()
