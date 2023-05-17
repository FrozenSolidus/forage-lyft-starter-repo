from ServiceableInterface import Serviceable
from CarFactory import CarFactory

class Car(Serviceable):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date
        self.factory = CarFactory()
    
    def needs_service(self) -> bool:
        return True
