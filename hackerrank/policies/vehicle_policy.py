


from datetime import datetime
from email import policy
from typing import List, Literal

from argon2 import Type
from numpy import require
from policies.base_policy import InsurancePolicy, PremiumCalculationRule, UnderWrittingRule


class VehiclePolicy(InsurancePolicy):
    def __init__(self, rules: List[UnderWrittingRule], premium_calculator: PremiumCalculationRule):
        super().__init__(rules, premium_calculator)
        self.__base_premium = 500.0
        
    def get_policy_type(self) -> Literal["vehicle", "house"]:
        return "vehicle"
    
    def validate_data(self, policy_data: dict) -> None:
        """Validate the data of the policy"""
        
        if not isinstance(policy_data, dict):
            raise TypeError("policy_data must be a dictionary")
        required_keys = ["age", "accident_history"]
        if not all(key in policy_data for key in required_keys):
            raise ValueError(f"policy_data must contain the keys: {required_keys}")
        if not isinstance(policy_data["age"], int):
            raise TypeError("age must be an integer")
        if not isinstance(policy_data["accident_history"], list):
            raise TypeError("accident_history must be a list")
        for accident in policy_data["accident_history"]:
            if not isinstance(accident, dict):
                raise TypeError("Each accident in accident_history must be a dictionary")
            if not all (key in accident for key in ["date", "at_fault"]):
                raise ValueError("Each accident must contain keys 'date' and 'at_fault'")
            try:
                datetime.strptime(accident["date"], '%Y-%m-%d')
            except ValueError:
                raise ValueError("Incorrect data format, should be YYYY-MM-DD in 'date'")
            if not isinstance(accident["at_fault"], bool):
                raise TypeError("at_fault must be a boolean value")
        