def average(numbers):
    """Calculates the average of a list of numbers."""
    if not numbers:
        raise ValueError("Empty list provided")
    return sum(numbers) / len(numbers)