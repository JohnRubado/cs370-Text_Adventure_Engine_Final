import os
class parser:
    def __init__(self, world):
        self.world = world

    def start(self,isNew):
        if isNew:
            print "\nWelcome to " + self.world.name + ". " + self.world.description;
            if len(self.world.areas) > 0:
                self.world.displayAreaDescription()
        else:
            print "Game loaded."
            if len(self.world.areas) > 0:
                self.world.displayAreaDescription()
        if self.world.loadScript != "":
            self.world.loadScript()
        while(True):
            userInput = raw_input()
            print "";
            userInput = userInput.lower().split()
            moveKeywords = ["move","go", "follow", "use"]
            lookKeywords = ["look", "show"]
            quitWords = ["quit"]
            helpWords = ["help"]
            takeWords = ["take", "pick"]
            dropWords = ["drop"]
            useWords = ["use"]
            inventoryWords = ["inventory"]
            noiseWords = ["at", "am", "here", "there", "to","through", "on", "up"]

            if len(userInput) == 0:
                continue

            for word in noiseWords:
                if word in userInput:
                    userInput.remove(word)

            if userInput[0] in useWords:

                if len(userInput) >= 3:
                    argument = ' '.join(userInput[2:])
                    name = userInput[1]
                    self.world.useItem(name,argument)
                elif len(userInput) == 2:
                    argument = ' '.join(userInput[1:])
                    self.world.movePlayer(argument)

            elif userInput[0] in moveKeywords:
                argument = ' '.join(userInput[1:])
                self.world.movePlayer(argument)

            elif userInput[0] in lookKeywords:
                argument = ' '.join(userInput[1:])
                if argument == '':
                    self.world.look()
                else:
                    self.world.look(argument)

            elif userInput[0] in quitWords:
                argument = ' '.join(userInput[1:])
                self.world.quitGame()

            elif userInput[0] in takeWords:
                argument = ' '.join(userInput[1:])
                self.world.pickUpItem(argument)

            elif userInput[0] in dropWords:
                argument = ' '.join(userInput[1:])
                self.world.dropItem(argument)

            elif userInput[0] in inventoryWords:
                argument = ' '.join(userInput[1:])
                self.world.checkInventory()

            elif userInput[0] in helpWords:
                argument = ' '.join(userInput[1:])
                self.world.helpUser()
            elif userInput[0] == "health":
                self.world.printHealth()
            elif userInput[0] == "score":
                self.world.printScore()
            elif userInput[0] == "save":
                self.world.saveProgress()
            elif userInput[0] == "load":
                if len(userInput) == 2:
                    loadFile = userInput[1]
                    loadFile = "./" + loadFile
                    if os.path.isfile(loadFile):
                        self.world.loadGame(loadFile)
                    else:
                        print "File " + userInput[1] + " does not exist."
                elif len(userInput) == 1:
                    print "Must provide file name to load"
            else:
                print "I don't know " + userInput[0]
