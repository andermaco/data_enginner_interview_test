from exceptions.insurance import CarToOldException, HomeRuleException, VehicleRuleException
from policies.vehicle_policy import VehiclePolicy
from policies.home_policy import HomePolicy
from rules.vehicle_rules import VehicleAgeRule, AccidentHistoryRule
from rules.home_rules import ParrotRule, BrokenWindowsRule
from calculators.vehicle_premium_calculator import VehiclePremiumCalculator
from calculators.home_premium_calculator import HomePremiumCalculator


# Vehicle Policy Example
vehicle_rules = [VehicleAgeRule(15), AccidentHistoryRule(2, 5)]
vehicle_calculator = VehiclePremiumCalculator(500.0)
vehicle_policy = VehiclePolicy(vehicle_rules, vehicle_calculator)

vehicle_sample_data = [
    {"age": 16, "accident_history": [{"date": "2023-04-23", "at_fault": False}]},
    {"age": 6, "accident_history": [{"date": "2022-07-20", "at_fault": True}, {"date": "2023-04-23", "at_fault": True}, {"date": "2024-02-23", "at_fault": True}]},
    {"age": 6, "accident_history": [{"date": "2022-07-20", "at_fault": False}, {"date": "2023-04-23", "at_fault": True}, {"date": "2024-01-12", "at_fault": False}]},
    {"age": 3, "accident_history": []}
]


for vehicle_data in vehicle_sample_data:
    try:
        vehicle_policy.validate_data(vehicle_data)
        print(f"{vehicle_data}  result: {vehicle_policy.calculate_premium(vehicle_data)}")
    except VehicleRuleException as e:
        print(f"{vehicle_data}  result: {e}")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")


# Home Policy Example
home_rules = [ParrotRule(5), BrokenWindowsRule()]
home_calculator = HomePremiumCalculator(300.0)
home_policy = HomePolicy(home_rules, home_calculator)

home_sample_data = [
    {"house_age": 16, "flood_risk": "HIGH", "n_parrots": 6, "windows": {"intact_windows": 5, "broken_windows": 0}},
    {"house_age": 52, "flood_risk": "LOW", "n_parrots": 0, "windows": {"intact_windows": 2, "broken_windows": 3}},  
    {"house_age": 25, "flood_risk": "MEDIUM", "n_parrots": 1, "windows": {"intact_windows": 4, "broken_windows": 1}},
    {"house_age": 3, "flood_risk": "LOW", "n_parrots": 0, "windows": {"intact_windows": 6, "broken_windows": 0}}
]

for home_data in home_sample_data:
    try:
        home_policy.validate_data(home_data)
        print(f"{home_data}  result: {home_policy.calculate_premium(home_data)}")
    except HomeRuleException as e:
        print(f"{home_data}  result: {e}")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")

    
# home_rules = [ParrotRule(5), BrokenWindowsRule()]
# home_calculator = HomePremiumCalculator(300.0)
# home_policy = HomePolicy(home_rules, home_calculator)

# home_data_1 = {"house_age": 16, "flood_risk": "HIGH", "n_parrots": 6, "windows": {"intact_windows": 5, "broken_windows": 0}}
# home_data_2 = {"house_age": 52, "flood_risk": "LOW", "n_parrots": 0, "windows": {"intact_windows": 2, "broken_windows": 3}}
# home_data_3 = {"house_age": 25, "flood_risk": "MEDIUM", "n_parrots": 1, "windows": {"intact_windows": 4, "broken_windows": 1}}
# home_data_4 = {"house_age": 3, "flood_risk": "LOW", "n_parrots": 0, "windows": {"intact_windows": 6, "broken_windows": 0}}

# try:
#     home_policy.validate_data(home_data_1)
#     print(f"Home Policy 1 Premium: {home_policy.calculate_premium(home_data_1)}<span class="math-inline">" if home\_policy\.calculate\_premium\(home\_data\_1\) else "Blocked by UW Rules"\)
# home\_policy\.validate\_data\(home\_data\_2\)
# print\(f"Home Policy 2 Premium\: \{home\_policy\.calculate\_premium\(home\_data\_2\)\}</span>" if home_policy.calculate_premium(home_data_2) else "Blocked by UW Rules")
#     home_policy.validate_data(home_data_3)
#     print(f"Home Policy 3 Premium: {home_policy.calculate_premium(home_data_3)}$"