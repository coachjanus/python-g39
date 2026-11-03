import random
from .analyzer import get_quartiles, calculate_upper_bound, trim_outliers

def main() -> None:
    print("Electricity Consumption Analyzer")

    # Generate mock monthly electricity consumption data with some outliers
    base_consumption = [random.uniform(150, 250) for _ in range(10)]
    outliers = [450.5, 600.2]
    monthly_data = base_consumption + outliers
    random.shuffle(monthly_data)

    # Format data for printing
    formatted_data = [round(val, 2) for val in monthly_data]
    print(f"\nOriginal Monthly Data (kWh):")
    print(formatted_data)
    
    # Functional pipeline
    q1, q3 = get_quartiles(monthly_data)
    max_acceptable_value = calculate_upper_bound(q1, q3)

    print(f"\nCalculated Q1: {q1:.2f}, Q3: {q3:.2f}")
    print(f"Maximum Acceptable Value (Upper Bound): {max_acceptable_value:.2f} kWh")

    # Trim the outliers
    trimmed_data = trim_outliers(monthly_data, max_acceptable_value)

    formatted_trimmed_data = [round(val, 2) for val in trimmed_data]
    print(f"\nTrimmed Monthly Data (kWh):")
    print(formatted_trimmed_data)
