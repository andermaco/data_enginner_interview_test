

from abc import ABC, abstractmethod
from email import policy
from typing import List, Literal
from unittest.mock import Base


class UnderWrittingRule(ABC):
    """Abstract class for underwriting rules"""
    
    @abstractmethod
    def is_approved(self, policy: dict) -> bool:
        pass

class PremiumCalculationRule(ABC):
    """Abstract class for premium calculation rules"""
    
    @abstractmethod
    def calculate_premium(self, policy: dict) -> float:
        pass
    
    
class InsurancePolicy(ABC):
    """Abstract class for insurance policies"""
    
    # policy_type = Literal["vehicle", "house"]
    policy_data = {}

    def __init__(self, rules: List[UnderWrittingRule], premium_calculator:PremiumCalculationRule):
        self._rules = rules
        self._premium_calculator = premium_calculator
    
    @abstractmethod
    def get_policy_type(self) -> Literal["vehicle", "house"]:
        """Return the type of the policy"""
        pass    

    @abstractmethod
    def validate_data(self, policy_data: dict) -> None:
        """Validate the data of the policy"""
        pass
    
    def is_policy_approved(self, policy_data: dict) -> bool:
        """Check if the policy is approved by all the underwriting rules"""
        for rule in self._rules:
            if not rule.is_approved(policy_data):
                return False
        return True
    
    def calculate_premium(self, policy_data: dict) -> float:
        """Calculate the premium of the policy"""
        
        if self.is_policy_approved(policy_data):
            """Check if the policy is approved by all the underwriting rules
            and calculate the premium"""            
            return self._premium_calculator.calculate_premium(policy_data)
        else:
            return 0.0