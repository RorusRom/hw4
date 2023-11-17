class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        raise NotImplementedError("Subclasses must implement this method")


class Machine:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def operate(self):
        raise NotImplementedError("Subclasses must implement this method")


class Robot(Animal, Machine):
    def __init__(self, name, species, brand, model):
        Animal.__init__(self, name, species)
        Machine.__init__(self, brand, model)

    def make_sound(self):
        return "Beep boop"

    def operate(self):
        return "Performing tasks autonomously"