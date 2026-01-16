def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if type(number) is not int or number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    
    #add to the proper divisors list only numbers where remainder is zero
    proper_divisors = [n for n in range (1, number) if number % n == 0]
    
    #ABUNDANT - less than aliquot sum
    if sum(proper_divisors) > number:
        return "abundant"
        
    #DEFICIENT - greater than aliquot sum (all primes)
    elif sum(proper_divisors) < number:
        return "deficient"
    
    #PERFECT - equals aliquot sum
    else:
        return "perfect"







