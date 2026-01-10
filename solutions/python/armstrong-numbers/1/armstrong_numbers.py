def is_armstrong_number(number):
    
    temp_sum = 0
    temp_number = number
    
    while temp_number > 0:
        temp_sum += (temp_number % 10)**len(str(number))
        temp_number = int(temp_number/10)
    
    return number == temp_sum







