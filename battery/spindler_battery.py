from abc import ABC

from battery.BatteryInterface import Battery
from datetime import date, timedelta


class SpindlerBattery(Battery):
    def __init__(self, last_service_date: date, current_date: date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        return (self.current_date - self.last_service_date) >= timedelta(days=365*3)