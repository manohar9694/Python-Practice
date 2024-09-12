########AGE CALCULATOR #########
from datetime import datetime

def calculate_age(birthdate):
    today = datetime.today()
    # Convert birthdate string to a datetime object
    birthdate = datetime.strptime(birthdate, "%Y-%m-%d")
    
    # Calculate the difference in years
    age = today.year - birthdate.year
    
    # Adjust if the birthday hasn't occurred yet this year
    if (today.month, today.day) < (birthdate.month, birthdate.day):
        age -= 1
    
    return age

# Example Usage:
dob = input("Enter your date of birth (YYYY-MM-DD): ")
age = calculate_age(dob)
print(f"You are {age} years old.")





