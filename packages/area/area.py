class Area:


    def __init__(self,name, description = "A vast land of wonders, maybe I should take a look around?"):
        self.name = name
        self.items = []
        self.transitions = []
        self.description = description


    #Adds transition to the list of transitions
    def newTransition(self, transition):
        self.transitions.append(transition)
