def get_median(data: list[float]) -> float:
    """Calculates the median of a list of numbers."""
    if not data:
        raise ValueError("Cannot calculate median of an empty list.")
    
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    
    if n % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2.0
    else:
        return sorted_data[mid]

def get_quartiles(data: list[float]) -> tuple[float, float]:
    """Calculates the first (Q1) and third (Q3) quartiles of a dataset."""
    if len(data) < 2:
        raise ValueError("Need at least 2 data points to calculate quartiles.")
    
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    
    # Using method 1 for quartile calculation: including median in both halves if odd parity is not relevant because we split exclusively
    if n % 2 == 0:
        lower_half = sorted_data[:mid]
        upper_half = sorted_data[mid:]
    else:
        lower_half = sorted_data[:mid]
        upper_half = sorted_data[mid+1:]
        
    q1 = get_median(lower_half)
    q3 = get_median(upper_half)
    
    return q1, q3

def calculate_upper_bound(q1: float, q3: float) -> float:
    """Calculates the maximum acceptable value using the IQR method."""
    iqr = q3 - q1
    return q3 + 1.5 * iqr

def trim_outliers(data: list[float], max_value: float) -> list[float]:
    """Trims outliers by replacing values exceeding max_value with max_value."""
    # Using map to apply the functional transformation
    return list(map(lambda x: min(x, max_value), data))
