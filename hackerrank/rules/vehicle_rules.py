from datetime import datetime, timedelta
from exceptions.insurance import CarDemotionDerbyException, CarToOldException
from policies.base_policy import UnderWrittingRule


class VehicleAgeRule(UnderWrittingRule):
    
    def __init__(self, max_age: int) -> None:
        self.max_age = max_age
    
    def is_approved(self, policy: dict) -> bool:        
        if policy["age"] <= self.max_age:
            return True
        raise CarToOldException()

class AccidentHistoryRule(UnderWrittingRule):
    
    def __init__(self, max_at_fault_accidents: int, period_years: int) -> None:
        self.max_at_fault_accidents = max_at_fault_accidents
        self.period_years = period_years
    
    def is_approved(self, policy: dict) -> bool:
        n_of_accidents = 0
        current_date = datetime.now()
        for accident in policy["accident_history"]:
            accident_date = datetime.strptime(accident["date"], '%Y-%m-%d')
            if accident["at_fault"] and (current_date - accident_date) <= timedelta(days=self.period_years * 365):
                n_of_accidents += 1
        if n_of_accidents < self.max_at_fault_accidents:
            return True
        raise CarDemotionDerbyException()