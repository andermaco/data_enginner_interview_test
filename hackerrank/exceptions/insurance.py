from abc import ABC, abstractmethod


class VehicleRuleException(ABC, Exception):
    def __init__(self, message: str = "") -> None:
        self.message = message
        super().__init__(message)

    def __str__(self) -> str:
        return self.message

class CarToOldException(VehicleRuleException):
    def __init__(self, message = "Blocked by UW Rules"):
        self.message = message
        # print("Car is too old")
    
class CarDemotionDerbyException(VehicleRuleException):
    def __init__(self, message = "Blocked by UW Rules"):
        self.message = message
        # print("Too many at-fault accidents in the last 5 years")
        
        
        
        
class HomeRuleException(ABC, Exception):
    def __init__(self, message = ""):
        self.message = message
        super().__init__(message)
    def __str__(self) -> str:
        return self.message    
        
        
class TooManyParrotsException(HomeRuleException):
    def __init__(self, message = "Blocked by UW Rules"):
        self.message = message
        # print("Too many parrots"")
        
class BrokenWindowsException(HomeRuleException):
    def __init__(self, message = "Blocked by UW Rules"):
        self.message = message
        # print("More broken windows than intact windows")
        
class FloodRiskException(HomeRuleException):
    def __init__(self, message = "Blocked by UW Rules"):
        self.message = message
        # print("Flood risk is too high")
        
class HouseAgeException(HomeRuleException):
    def __init__(self, message = "Blocked by UW Rules"):
        self.message = message
        # print("House is too old")
        
        