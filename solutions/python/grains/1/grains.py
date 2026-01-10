def square(number):
    if not 0 < number <= 64:
        raise ValueError("square must be between 1 and 64")

    return 2**(number-1)

def total():
    i=1
    total_grains=0
    while i <= 64:
        total_grains += 2**(i-1)
        i += 1
    return total_grains