# Import datetime so that it can be
# used to compute a person's age.
from datetime import datetime


def main():
    # Get the user's gender, birthdate, height, and weight.
    gender = input('\nPlease enter your gender (F/M): ')
    b_day = input('Please enter your BirthDate in YYYY-MM-DD format:')
    height_ft = float(input('please enter your Height in US Feet: '))
    height_in = float(input('please enter your Height in US Inches: '))
    weight = float(input('Please enther your Weight in LBS : '))
    # Call the compute_age, kg_from_lb, cm_from_in,
    # body_mass_index, and basal_metabolic_rate functions
    # as needed.
    age = compute_age(b_day)
    kg = kg_from_lb(weight)
    stones = stones_to_pounds(weight)
    inches = inches_from_feet_and_inches(height_ft, height_in)
    cm = cm_from_in(inches)
    BMI = body_mass_index(kg, cm)
    BMR = basal_metabolic_rate(gender,kg, cm, age)
    height_meters = cm_to_meters(cm)
    # Print the results for the user to see.
    print(f'\nYour age: {age}')
    print(f'Weight {stones :.2f} British Stones')
    print(f'Weight (kg): {kg:.1f}')
    print(f'Height (meters): {height_meters:.2f}')
    print(f'Body mass index: {BMI:.2f}')
    print(f'Basal metabolic rate (kcal/day): {BMR:.2f}')
    pass


def compute_age(birth_str):
    """Compute and return a person's age in years.
    Parameter birth_str: a person's birthdate stored
        as a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    # Convert a person's birthdate from a string
    # to a date object.
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.now()

    # Compute the difference between today and the
    # person's birthdate in years.
    years = today.year - birthdate.year

    # If necessary, subtract one from the difference.
    if birthdate.month > today.month or \
        (birthdate.month == today.month and \
            birthdate.day > today.day):
        years -= 1

    return years

def stones_to_pounds(weight):
    stones = weight/14
    return stones


def kg_from_lb(pounds):
    """Convert a mass in pounds to kilograms.
    Parameter pounds: a mass in U.S. pounds.
    Return: the mass in kilograms.
    """
    kg = pounds / 2.205

    return kg

def inches_from_feet_and_inches(feet,inches):
    inches = (feet*12) + inches
    return inches

def cm_from_in(inches):
    """Convert a length in inches to centimeters.
    Parameter inches: a length in inches.
    Return: the length in centimeters.
    """
    cm = inches * 2.54
    

    return cm

def cm_to_meters(cm):
    meters = cm / 100
    return meters

def body_mass_index(weight, height):
    """Compute and return a person's body mass index.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
    Return: a person's body mass index.
    """
    bmi = ((10000*weight)/(height**2))
    return bmi


def basal_metabolic_rate(gender, weight, height, age):
    """Compute and return a person's basal metabolic rate.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
        age: a person's age in years.
    Return: a person's basal metabolic rate in kcals per day.
    """
    if gender.lower == 'm':
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else: 
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    return bmr


# Call the main function so that
# this program will start executing.
main()