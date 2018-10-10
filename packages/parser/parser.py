import os
class parser:
    def __init__(self, world):
        self.world = world

    def start(self):
        print "\nWelcome to " + self.world.name + ". " + self.world.description;
        self.world.displayAreaDescription()
        self.world.loadScript()
        while(True):
            userInput = raw_input()
            print "";
            userInput = userInput.lower().split()
            moveKeywords = ["move","go", "use"]
            lookKeywords = ["look", "show"]
            noiseWords = ["at", "am", "here", "there"]
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
            else:
                print "I don't know " + userInput[0]
