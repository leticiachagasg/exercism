def leap_year(year):
    """
    Function to determine whether a given year is a leap year
    
    :param year: int year
    """
    
    if year % 4 != 0:
        return False
    elif year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False


