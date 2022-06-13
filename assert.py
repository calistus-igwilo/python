#######################
# Asert
#######################
"""
Assert the is_italy variable using the assert statement
"""
countries = ['POL', 'ENG', 'GER', 'USA', 'ITA']
is_italy = 'ITA' in countries

assert is_italy, f'ITA expected to be in the list of countries'


"""
The implementation of the max_min_diff() function is given:

def max_min_diff(numbers):
    # enter your solution here
    return max(numbers) - min(numbers)

Modify the implementation of the max_min_diff() function. By using the
assert statement inside this function, add the ability to check the 
length of the numbers arguement before retruning the result. If the
length of the numbers object is 0 raise the AssertionErrorw without
any message. Otherwise return the correct result.

In response, call max_min_diff() function passin an empty list
"""
def max_min_diff(numbers):
    assert len(numbers) != 0
    return max(numbers) - min(numbers)
max_min_diff([])


"""
The following area() function is given, which returns the area of a 
rectangle (no argument validation).

    def area(width, height):
        return width * height
Assert the following funtion calls:
    area(4, 10)
    area(5, 6)
with the appropriate values:
    40
    30
"""
def area(width, height):
    return width * height

assert area(4, 10) == 40
assert area(5, 6) == 30


"""
The following area function is given which returns the area of a 
rectangle with additional argument validation:

def area(width, height):
    '''The function returns the area of the rectangle.'''

    if not (isinstance(width, int) and isinstance(height, int)):
        raise TypeError('The width and height must be of type int.')

    if not (width > 0 and height > 0):
        raise ValueError('The width and height must be positive.')

    return width * height

Assert the following function call:
    area('5', '4')
with value of 20
"""
def area(width, height):
    """The function returns the area of the rectangle."""

    if not (isinstance(width, int) and isinstance(height, int)):
        raise TypeError('The width and height must be of type int.')

    if not (width > 0 and height > 0):
        raise ValueError('The width and height must be positive.')

    return width * height

assert area('5', '4') == 20

area('5', '4')
