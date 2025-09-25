import math

def validate_age(age):
    """
    This function vaildates age as an integer.
    Add integer and it will check it is a positive number and not a decimal.
    ValueError for none ages.
    """

    # check if age is an integer
        # if not integer raise error
    if not isinstance(age, int):   
        raise ValueError("Age must be an integer")
    # check if integer is positive
        # if not positive raise error
    if age <=0:
        raise ValueError("Age must be positive integer")
    return age

# print(validate_age(31))

def calculate_rectangle_area(length, width):
    return length * width

def calculate_circle_area(radius):
    return math.pi * (radius * radius)

def get_area(shape, *args):
    # make sure shape is rectangle or circle
    # normalize the input
    shape=shape.lower().strip()
    
    if shape == "rectangle":
    # if it's rectangle extract l & w from args
        length, width = args
        # then pass values to calculate area
        return calculate_rectangle_area(length, width)
    else:
    # if it's circle extract radius from args
        # then pass value to calculate circle area
        # assign a radius variable to the first index of args
        # use index positioning to extract radius
        radius = args[0]
        return calculate_circle_area(radius)

# print(get_area("circle", 23))
# pgit add -Arint(get_area("rectangle", 12, 10))