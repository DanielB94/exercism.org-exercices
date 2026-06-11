"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


EXPECTED_BAKE_TIME = 40

def bake_time_remaining(current_time):
    
    """Calculate the elapsed cooking time.
    Parameters:
        current_time: time has been already consumed making the lasagna
    
    Returns:
        int: te time remaining for lasagna to be ready
    
    """
    return EXPECTED_BAKE_TIME - current_time

def preparation_time_in_minutes(number_of_layers):
    """Calculate the elapsed cooking time.
    
    Parameters:
        number_of_layers (int): The number of layers in the lasagna.
    
    Returns:
        int: the time any lasagna layer would take to make
    
    """
    return number_of_layers * 2

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed cooking time.
    
    Parameters:
        number_of_layers (int): The number of layers in the lasagna.
        elapsed_bake_time (int): Time the lasagna has been baking in the oven.
    
    Returns:
        int: The total time elapsed (in minutes) preparing and baking.

    This function takes two integers representing the number of lasagna 
    layers and the time already spent baking the lasagna. It calculates 
    the total elapsed minutes spent cooking (preparing + baking).
    
    """
    layers_time = number_of_layers * 2
    return layers_time + elapsed_bake_time
