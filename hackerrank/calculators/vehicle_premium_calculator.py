

import re
from numpy import rec
from policies.base_policy import PremiumCalculationRule
from datetime import datetime, timedelta

class VehiclePremiumCalculator(PremiumCalculationRule):
    
    def __init__(self, base_premium: float) -> None:
        self.base_premium = base_premium
    
    def calculate_premium(self, policy: dict) -> float:
        premium = 0.0    
        # Vintage factor
        vintage_factor = 0.0
        if policy["age"] > 5: 
            vintage_factor += (policy["age"] - 5) * 0.05
        
        # Crash course fee
        recent_accidents = 0
        current_date = datetime.now()
        for accident in policy["accident_history"]:
            accident_date = datetime.strptime(accident["date"], '%Y-%m-%d')

            """ Here it is, the requirements says 
            -Apply a 20% crash course fee for each accident in the last 3 years (because we believe in paying for our mistakes).
            So, based on the requirements, we should only apply the 20% fee if the accident is at fault OR NOT and happened in the last 3 years.
            """
            if accident["at_fault"] and (current_date - accident_date) <= timedelta(days= 3 * 365):
            # if (current_date - accident_date) <= timedelta(days= 3 * 365):
                recent_accidents += 1
        # premium += self.base_premium * (1 + vintage_factor + recent_accidents * 0.2)
        premium += (self.base_premium * (1 + vintage_factor)) * (1 + recent_accidents * 0.2)
        return round(premium, 2)