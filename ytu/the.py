class vehicle():
    def __init__(self, bodystyle):
        self.bodystyle = bodystyle

    def drive(self, speed):
        self.mode = "driving"
        self.speed = speed
        
class car(vehicle):
    def __init__(self, enginetype):
        super().__init__("car")
        self.wheel = 4
        self.doors = 4
        self.enginetype = enginetype
    
    def drive(self, speed):
        super().drive(speed)
        print("driving my", self.enginetype, "car at", self.speed)

class motorcycle(vehicle):
    def __init__(self, enginetype, sidecar ):
        super().__init__("motorcycle")
        if (sidecar):
            self.wheel = 3
        else:
            self.wheel = 2
            self.door = 0
            self.enginetype = enginetype
   
    def drive(self, speed):
        super().drive(speed)
        print("driving my", self.enginetype, "motorcycle at", self.speed)

car1 = car("gas")
mc1 = motorcycle("gas", True)

print(mc1.wheel)
print(car1.enginetype)

car1.drive = 30
mc1.drive = 50

