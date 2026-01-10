def equilateral(sides):
    """
    Function that evaluates if a triangle is equilateral based on its given sides

    :param sides: list of tree items representing each side of a triangle
    """
    
    a = sides[0]
    b = sides[1]
    c = sides [2]
    
    if not a + b >= c or not b + c >= a or not a + c >= b:
        return False
    elif a <= 0 or b <= 0 or c <= 0:
        return False
    else:
        return a == b == c


def isosceles(sides):
    """
    Function that evaluates if a triangle is isosceles based on its given sides

    :param sides: list of tree items representing each side of a triangle
    """
    
    a = sides[0]
    b = sides[1]
    c = sides [2]
    
    if not a + b >= c or not b + c >= a or not a + c >= b:
        return False
    elif a <= 0 or b <= 0 or c <= 0:
        return False
    else:
        
     a_repeats = a == b or a == c
     b_repeats = b == a or b == c
     c_repeats = c == b or c == a
        
    return int(a_repeats) + int(b_repeats) + int(c_repeats) > 1


def scalene(sides):
    """
    Function that evaluates if a triangle is scalene based on its given sides

    :param sides: list of tree items representing each side of a triangle
    """
    
    a = sides[0]
    b = sides[1]
    c = sides [2]   
    
    
    if not a + b >= c or not b + c >= a or not a + c >= b:
        return False
    elif a <= 0 or b <= 0 or c <= 0:
        return False
    else:
        return (a != b != c != a)



