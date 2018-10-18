class Area:


    def __init__(self,name, description = "A vast land of wonders, maybe I should take a look around?"):
        self.name = name
        self.transitions = []
        self.description = description
        self.inAreaScripts = []


    def setDescription(self, description =""):
        self.description = description


    #Adds transition to the list of transitions
    def newTransition(self, transition):
        self.transitions.append(transition)

    def printArea(self):
        print("You are in the " +self.name + ". " + self.description)

        for transition in self.transitions:
            transition.printTrans(transition)
