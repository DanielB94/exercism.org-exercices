def find(search_list: list[int], value: int) -> int:
    """Finds the index of a value in a sorted list using binary search.

    Args:
        search_list (list[int]): A sorted list of integers.
        value (int): The target integer to locate.

    Returns:
        int: The index of the target value.

    Raises:
        ValueError: If the value is not present in the list. """
    
    low: int = 0
    high: int = len(search_list) - 1

    while low <= high:
        mid = (low + high) // 2
        if search_list[mid] == value:
            return mid
        elif search_list[mid] < value:
            low = mid + 1
        else:
            high = mid - 1
    raise ValueError("value not in array")  
