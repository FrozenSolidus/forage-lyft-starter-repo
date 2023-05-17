from ServiceableInterface import Serviceable

class Car(Serviceable):
    def __init__(self, engine, battery, tires):
        self.engine = engine
        self.battery = battery
        self.tires = tires
    
    def needs_service(self):
        if self.engine.needs_service(): return True
        if self.battery.needs_service(): return True
        if self.tires.needs_service(): return True
