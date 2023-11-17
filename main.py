class Anim:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        raise NotImplementedError("Subclasses must implement this method")


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def operate(self):
        raise NotImplementedError("Subclasses must implement this method")


class Robot(Anim, Car):
    def __init__(self, name, species, brand, model):
        Anim.__init__(self, name, species)
        Car.__init__(self, brand, model)

    def make_sound(self):
        return "Beep boop"

    def operate(self):
        return "Performing tasks autonomously"
