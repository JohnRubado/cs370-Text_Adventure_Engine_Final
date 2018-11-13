from packages.item.item import item

class Area:


    def __init__(self,name, description = "A vast land of wonders, maybe I should take a look around?"):
        self.name = name
        self.transitions = []
        self.description = description
        self.items = []
        self.inAreaScripts = []



    def setDescription(self, description =""):
        self.description = description


    #Adds transition to the list of transitions
    def newTransition(self, transition):
        self.transitions.append(transition)

    def newItem(self, item):
        self.items.append(item)

    def printArea(self):
        print("You are in the " +self.name + ". " + self.description)

        for transition in self.transitions:

            #if the transition is blocked....
            if len(transition.requirements) >= 1:
                transition.printDescription()
            else:
                if transition.openedDescription != None:
                    transition.printOpenedDescription()
                else:
                    transition.printDescription()
        for item in self.items:
            item.printDescription()

    def removeItem(self, item):
        item.area = None
        self.items.remove(item)
