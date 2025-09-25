import random, datetime, math
def generate_password(password_length):
    # list of uppercase letters
    lower_case_letters = "abcdefghijklmnopqrstuvwxyz"
    upper_case_letters = lower_case_letters.upper()
    digits = "0123456789"
    

    if not isinstance(password_length, int):
        raise ValueError("password_length must be an integer")
    if password_length < 8:
        raise ValueError("password length must be 8 or more")
     
    chars = lower_case_letters + upper_case_letters + digits

    
    password = "".join(random.choice(chars) for char in range(password_length))
       

    return password

# print(generate_password(9))

def days_between(day_1, day_2):
    day_1 = datetime.datetime.strptime(day_1, "%Y-%m-%d") 
    day_2 = datetime.datetime.strptime(day_2, "%Y-%m-%d")  

    return (day_1 - day_2)

# print(days_between("2025-09-22", "2025-09-9"))

def calculate_circle_area(radius):
    return math.pi * (radius ** 2)

print(calculate_circle_area(50))