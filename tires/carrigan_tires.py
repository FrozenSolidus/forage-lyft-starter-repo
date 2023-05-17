from abc import ABC

from tires.TiresInterface import Tires


class CarriganTires(Tires):
    def __init__(self, tires):
        self.tires = tires

    def needs_service(self):
        for num in self.tires:
            if num >= 0.9:
                return True
        return False