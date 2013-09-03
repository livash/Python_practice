# Practive python methods

def square_return(num):
    return num ** 2
    
def print_square(num):
    print(num ** 2)

print_square(4)

# using doc string in a function

def area_triangle(base, height):
    '''(number, number) -> number
    Returns an area of a triengle with
    dimentions base and height
    '''
    return 0.5 * base * height
    
print("Triange area is", area_triangle(2,5))

def convert_to_celsius(fahrenheit):
    """(number) -> float
    Return fahrenheit value converted to celsius
    
    >>> convert_to_celsius(32)
    0.0
    >>> convert_to_celsius(212)
    100.0
    """
    return (fahrenheit - 32) * 5 / 9
    
print(convert_to_celsius(32))
print(convert_to_celsius(33))
print(convert_to_celsius(212))