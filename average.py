def average(values):
    """Calculates the average of values in a list."""
    if not values:
        raise ValueError("Empty list provided")
    return sum(values) / len(values)