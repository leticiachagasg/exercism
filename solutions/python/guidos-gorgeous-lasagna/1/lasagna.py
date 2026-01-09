"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    
    if not type(elapsed_bake_time) == int:
        raise TypeError("Elapsed time must be an integer")
    
    if elapsed_bake_time < 0:
        raise ValueError("Elapsed bake time cannot be negative")
    
    if elapsed_bake_time > EXPECTED_BAKE_TIME:
        raise ValueError(f"Elapsed bake time should not exceed {EXPECTED_BAKE_TIME} minutes")
    

    
    remaining_time = EXPECTED_BAKE_TIME - elapsed_bake_time

    return remaining_time


def preparation_time_in_minutes(number_of_layers):
    """Calculate the time to prepare the lasanha based on the number of layers.

    :param number_of_layers: int - how many layers the lasagna will have.
    :return: int - preparation time (in minutes) derived from 'PREPARATION_TIME'.

    Function that takes the number of layers that a lasagna will have as an argument and returns how many minutes the preparation will take based on `PREPARATION_TIME`.
    """
    
    if not type(number_of_layers) == int:
        raise TypeError("Number of layers must be an integer")
    
    if number_of_layers < 0:
        raise ValueError("Number of layers cannot be negative")
    
    preparation_time = number_of_layers * PREPARATION_TIME
    
    return preparation_time



def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time): 
    """Calculate the total cooking time spent preparing and baking the lasagna.

    :param number_of_layers: int - how many layers the lasagna has.
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - total time spent cooking.

    Function that takes the preparation time layering + the time the lasagna has spent baking in the over and returns the total time in minutes spent in the kitchen cooking
    """
    
    if not type(number_of_layers) == int:
        raise TypeError("Number of layers must be an integer")
    
    if number_of_layers < 0:
        raise ValueError("Number of layers cannot be negative")
    
    if not type(elapsed_bake_time) == int:
        raise TypeError("Elapsed time must be an integer")
    
    if elapsed_bake_time < 0:
        raise ValueError("Elapsed bake time cannot be negative")
    
    total_time_cooking = preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
    
    return total_time_cooking
    


