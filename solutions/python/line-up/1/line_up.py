def line_up(name: str, number: int) -> str:
    """Format a customer's queue status using proper English ordinal numbers.

    Args:
        name: Customer's name.
        number: Queue position (1 to 999).

    Returns:
        Formatted announcement string.
    """
    
    if number % 100 in (11, 12, 13):
        suffix: str = 'th'
    else:
        suffix = {1: 'st', 2: 'nd', 3:'rd'}.get(number % 10, 'th')

    return f"{name}, you are the {number}{suffix} customer we serve today. Thank you!"