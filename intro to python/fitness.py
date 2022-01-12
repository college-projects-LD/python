# Import datetime so that it can be
# used to compute a person's age.
from datetime import datetime


def main():
    # Get the user's gender, birthdate, height, and weight.

    # Call the compute_age, kg_from_lb, cm_from_in, body_mass_index,
    # and basal_metabolic_rate functions as needed.

    # Print the results for the user to see.
    gender = input('Please enter your gender : ')
    birth = input('Please enter your birthdate (YYYY-MM-DD) : ')
    inch = float(input(' please enter your height in inches : '))
    lb = float(input('please enter your weight in Pounds : '))
    weight = kg_from_lb(lb)
    height = cm_from_in(inch)
    age = compute_age(birth)

    print(f'Age (years) : {age}')
    print(f'Weight (kg) : {weight}')
    print (f'Height(cm) : {height}')
    print(f'Bmi : {body_mass_index(weight,height)}')
    print (f'Basal metabolic rate (kcal/day) : {basal_metabolic_rate(gender, weight, height, age)}')


def compute_age(birth):
    """Compute and return a person's age in years.
    Parameter birth: a person's birthdate stored as
        a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    birthday = datetime.strptime(birth, "%Y-%m-%d")
    today = datetime.now()

    # Compute the difference between today and the birthday in years.
    years = today.year - birthday.year

    # If necessary, subtract one from the difference.
    if birthday.month > today.month or \
        (birthday.month == today.month and birthday.day > today.day):
        years -= 1

    return years


def kg_from_lb(lb):
    """Convert a mass in pounds to kilograms.
    Parameter lb: a mass in US pounds.
    Return: the mass in kilograms.
    """
    kg = lb * 0.45359237
    Kg = round(kg,2)
    return Kg
    


def cm_from_in(inch):
    """Convert a length in inches to centimeters.
    Parameter inch: a length in inches.
    Return: the length in centimeters.
    """
    cm = inch *2.54
    cm = round(cm,2)
    return cm


def body_mass_index(weight, height):
    """Calculate and return a person's body mass index (bmi).
    Parameters:
        weight must be in kilograms.
        height must be in centimeters.
    Return: a person's body mass index.
    """
    bmi = (10000*weight)/ (height**2)
    bmi = round(bmi,2)
    return bmi


def basal_metabolic_rate(gender, weight, height, age):
    """Calculate and return a person's basal metabolic rate (bmr).
    Parameters:
        weight must be in kilograms.
        height must be in centimeters.
        age must be in years.
    Return: a person's basal metabolic rate in kcal per day.
    """
    if gender.lower() == ('f'):
        bmr = 447.593 + 9.247 * weight + 3.098*height - 4.330* age
    
    else:
        bmr = 88.362 + 13.397*weight + 4.799*height - 5.677*age
    bmr = round(bmr,2)
    return bmr


# Call the main function so that
# this program will start executing.
main()
