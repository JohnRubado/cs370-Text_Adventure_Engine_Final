

class transition:

    def __init__(self, name, area, direction, description = "It must lead somewhere" , destination):
        self.name = name
        self.area = area
        self.direction = direction
        self.destination = destination
        self.requirements = []
