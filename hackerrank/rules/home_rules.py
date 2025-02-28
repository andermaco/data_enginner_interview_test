
from exceptions.insurance import BrokenWindowsException, TooManyParrotsException
from policies.base_policy import UnderWrittingRule


class ParrotRule(UnderWrittingRule):
    def __init__(self, max_parrots: int):
        self.max_parrots = max_parrots

    def is_approved(self, policy_data: dict) -> bool:
        if policy_data["n_parrots"] <= self.max_parrots:
            return True
        raise TooManyParrotsException()
    
class BrokenWindowsRule(UnderWrittingRule):
    def is_approved(self, policy_data: dict) -> bool:
        if policy_data["windows"]["broken_windows"] <= policy_data["windows"]["intact_windows"]:
            return True
        raise BrokenWindowsException()
    
class FloodRiskRule(UnderWrittingRule):
    def __init__(self, max_flood_risk: str):
        self.max_flood_risk = max_flood_risk

    def is_approved(self, policy_data: dict) -> bool:
        return policy_data["flood_risk"] <= self.max_flood_risk
    
class HouseAgeRule(UnderWrittingRule):
    def __init__(self, min_house_age: int):
        self.min_house_age = min_house_age
