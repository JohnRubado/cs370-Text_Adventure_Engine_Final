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
        self.world.loadScript()
        while(True):
            userInput = raw_input()
            print "";
            userInput = userInput.lower().split()
            moveKeywords = ["move","go", "use"]
            lookKeywords = ["look", "show"]
            noiseWords = ["at", "am", "here", "there", "to"]
            if len(userInput) == 0:
                continue
            for word in noiseWords:
                if word in userInput:
                    userInput.remove(word)
            if userInput[0] in moveKeywords:
                argument = ' '.join(userInput[1:])
                self.world.movePlayer(argument)

            elif userInput[0] in lookKeywords:
                argument = ' '.join(userInput[1:])
                if argument == '':
                    self.world.look()
                else:
                    self.world.look(argument)
            elif userInput[0] == "save":
                self.world.saveProgress()
            elif userInput[0] == "load":
                if len(userInput) == 2:
                    loadFile = userInput[1]
                    loadFile = "./" + loadFile
                    if os.path.isfile(loadFile):
                        self.world.loadGame(loadFile)
                elif len(userInput) == 1:
                    print "Must provide file name to load"


            else:
                print "I don't know " + userInput[0]
