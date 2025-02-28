

from policies.base_policy import PremiumCalculationRule


class HomePremiumCalculator(PremiumCalculationRule):
    
    def __init__(self, base_premium: float) -> None:
        self.base_premium = base_premium
    
    def calculate_premium(self, policy: dict) -> float:
        premium = self.base_premium
        # Flood risk surcharge
        if policy["flood_risk"] == "MEDIUM":
            premium *= 1.15
        # Retro surcharge
        if policy["house_age"] > 20:
            premium *= 1.10
        return round(premium,2)