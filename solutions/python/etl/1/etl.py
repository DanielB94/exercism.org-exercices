def transform(legacy_data: dict[int, list[str]]) -> dict[str: int]:
    """Transform Scrabble score data from legacy format to new format.

    Takes a dictionary mapping point values to lists of uppercase letters
    and converts it into a dictionary mapping individual lowercase letters
    to their corresponding point values.

    Args:
        legacy_data: A dictionary where keys are point scores (int)
            and values are lists of letters (list[str]).

    Returns:
        A dictionary mapping each lowercase letter (str) to its score (int).
        """
    return {letter.lower(): points for points, letters in legacy_data.items() for letter in letters}
