class Car:

    def __init__(self):
        self.active = False
        self.kilometers = 0

    def turn_on(self):
        if not self.active:
            self.active = True
        return self.active

    def turn_off(self):
        if self.active:
            self.active = False
        return self.active

    def move(self,meters):
        if self.active:
            self.kilometers = self.kilometers + (meters/0.001)
            return True
        return False
