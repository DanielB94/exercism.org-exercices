from datetime import datetime, timedelta

def add(moment: datetime) -> datetime:
    """Calculates the date and time after adding one gigasecond (10^9 seconds) to a given moment.

    Args:
        moment (datetime): The starting date and time.

    Returns:
        datetime: The resulting date and time exactly 1,000,000,000 seconds later."""
    return moment + timedelta(seconds=10**9)
