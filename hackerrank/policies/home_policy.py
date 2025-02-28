from policies.base_policy import InsurancePolicy, UnderWrittingRule, PremiumCalculationRule
from typing import List, Dict, Literal

class HomePolicy(InsurancePolicy):
    """Represents a home insurance policy."""
    def __init__(self, rules: List[UnderWrittingRule], calculator: PremiumCalculationRule):
        super().__init__(rules, calculator)
        self.base_premium = 300.0

    def get_policy_type(self) -> Literal["vehicle", "house"]:
        return "house"

    def validate_data(self, policy_data: dict) -> None:
        if not isinstance(policy_data, dict):
            raise TypeError("policy_data must be a dictionary")
        required_keys = ["house_age", "flood_risk", "n_parrots", "windows"]
        if not all(key in policy_data for key in required_keys):
            raise ValueError(f"Missing required keys in policy_data: {required_keys}")

        if not isinstance(policy_data["house_age"], int):
            raise TypeError("house_age must be an integer.")
        if not isinstance(policy_data["flood_risk"], str):
            raise TypeError("flood_risk must be a string.")
        if policy_data["flood_risk"] not in ["LOW", "MEDIUM", "HIGH"]:
            raise ValueError("flood_risk must be 'LOW', 'MEDIUM', or 'HIGH'.")
        if not isinstance(policy_data["n_parrots"], int):
            raise TypeError("n_parrots must be an integer.")
        if not isinstance(policy_data["windows"], dict):
            raise TypeError("windows must be a dictionary.")
        if not all(key in policy_data["windows"] for key in ["intact_windows", "broken_windows"]):
            raise ValueError("windows must contain keys 'intact_windows' and 'broken_windows'.")
        if not isinstance(policy_data["windows"]["intact_windows"], int):
            raise TypeError("intact_windows must be an integer")
        if not isinstance(policy_data["windows"]["broken_windows"], int):
            raise TypeError("broken_windows must be an integer")